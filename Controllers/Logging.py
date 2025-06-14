from Encryption.Encryptor import Decrypt, Encrypt
from datetime import datetime, timezone


logFilePath = "./Logs/log.txt"
suspiciousFilePath = "./Logs/suspiciousLog.txt"

def logString(message, critical = False):
    # Encrypt the message
    encrypted_message = Encrypt(message)
    
    # Write the encrypted message to the log file
    with open(logFilePath, "ab") as logFile:  # 'ab' mode to append in binary format
        logFile.write(encrypted_message + b"\n")
    if (critical):
        with open(suspiciousFilePath, "ab") as logFile:  # 'ab' mode to append in binary format
            logFile.write(encrypted_message + b"\n")

def log(description:str, Username:str = "", additional:str = "", critical:bool = False ):
    # Get the current date and time
    current_datetime = datetime.now(timezone.utc)

    # Extract date and time separately
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    suspicious = "Yes" if critical else "no"

    logString(f"{current_date}, {current_time}, {Username}, {description}, {additional}, {suspicious}")


def readLog():
    # create empty list
    decryptedLines = []
    # open file with 'rb' to read binary
    with open(logFilePath, "rb") as logFile:
        # read out the lines
        lines = logFile.readlines()
        # loop through the lines to decrypt and add to list
        for line in lines:
            decryptedLine = Decrypt(line.strip())
            decryptedLines.append(decryptedLine)
    # return decrypted list
    return decryptedLines

def readSuspiciousLog():
    # create empty list
    decryptedLines = []
    # open file with 'rb' to read binary
    with open(suspiciousFilePath, "rb") as logFile:
        # read out the lines
        lines = logFile.readlines()
        # loop through the lines to decrypt and add to list
        for line in lines:
            decryptedLine = Decrypt(line.strip())
            decryptedLines.append(decryptedLine)
    # return decrypted list
    return decryptedLines