import Controllers.Encryptions as Encryptions
import os

logFilePath = "./Logs/log.txt"

def logString(message):
    # Encrypt the message
    encrypted_message = Encryptions.encrypt(message)
    
    # Write the encrypted message to the log file
    with open(logFilePath, "ab") as logFile:  # 'ab' mode to append in binary format
        logFile.write(encrypted_message + b"\n")

def readLog():
    # create empty list
    decryptedLines = []
    # open file with 'rb' to read binary
    with open(logFilePath, "rb") as logFile:
        # read out the lines
        lines = logFile.readlines()
        # loop through the lines to decrypt and add to list
        for line in lines:
            decryptedLine = Encryptions.decrypt(line.strip())
            decryptedLines.append(decryptedLine)
    # return decrypted list
    return decryptedLines
