import os
from sqlite3 import Connection, Cursor
from Encryption.Encryptor import Decrypt, Encrypt
from datetime import datetime, timezone
from cryptography.exceptions import InvalidTag

from Model.Last_Read_Log import findLastReadLog, upsertLastReadLog
from Model.Logs import insertLog
from Model.Suspicious_Logs import insertSusLog


def logString(connection, message, critical=False):
    # Encrypt the message
    encrypted_message = Encrypt(message)

    if (critical):
        insertSusLog(connection, encrypted_message)
    else:
        insertLog(connection, encrypted_message)


def log(connection, description: str, Username: str = "", additional: str = "", critical: bool = False):
    # Get the current date and time
    current_datetime = datetime.now(timezone.utc)

    # Extract date and time separately
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    suspicious = "Yes" if critical == True else "no"

    logString(connection, f"{current_date}, {current_time}, {Username}, {description}, {additional}, {suspicious}", critical)


def readLog(cursor:Cursor):
    # create empty list
    decryptedLines = []
    # open file with 'rb' to read binary
    lines = cursor.execute("""
        SELECT * FROM Logs
    """).fetchall()

    # loop through the lines to decrypt and add to list
    for line in lines:
        try:
            decryptedLine = Decrypt(line[0])
        except InvalidTag:
            decryptedLine = "corrupted log"
        decryptedLines.append(decryptedLine)
    # return decrypted list
    return decryptedLines


def readSuspiciousLog(connection:Connection, username:str):
    upsertLastReadLog(connection, username)

        # create empty list
    decryptedLines = []
    # open file with 'rb' to read binary
    lines = connection.cursor().execute("""
        SELECT * FROM Suspicious_logs
    """).fetchall()

    # loop through the lines to decrypt and add to list
    for line in lines:
        try:
            decryptedLine = Decrypt(line[0])
        except InvalidTag:
            decryptedLine = "corrupted log"
        decryptedLines.append(decryptedLine)
    # return decrypted list
    return decryptedLines


def checkIfUnreadSuspiciousLogs(connection:Connection, username:str):
    LastReadLog = findLastReadLog(connection.cursor(), username)

    # check if any of the logs are dated after the Last Read date
    try:
        # Read and decrypt all lines using readSuspiciousLog
        decrypted_lines = readSuspiciousLog(connection, username)
        if (len(decrypted_lines) == 0):
            return False
        elif (LastReadLog is None):
            return True
        
        # Loop through each decrypted line
        for decrypted_line in decrypted_lines:
            if (decrypted_line == "corrupted log"):
                continue
            try:
                # Convert each decrypted line to datetime
                parts = [part.strip() for part in decrypted_line.split(',')]
                # Combine the date and time parts
                date_time_str = parts[0] + ' ' + parts[1]
                # Convert to datetime object
                line_datetime = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

                # Check if the line's datetime is after LastRead
                if line_datetime > LastReadLog.Read_date.replace(tzinfo=None):
                    return True
            except ValueError:
                # Skip lines that cannot be parsed as datetime
                continue
    except Exception:
        # Handle unexpected issues
        return False
    return False