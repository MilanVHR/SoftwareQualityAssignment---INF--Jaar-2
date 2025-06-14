import re

def isPasswordValid(password) :
    pattern = r"^(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[\d])(?=.*[~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/])[a-zA-Z\d~!@#$%&_\-+=`|\\(){}\[\]:;'<>,.?/]{8,30}$"
    if re.match(pattern, password):
        return True
    else:
        return False

def isdriversLicenseValid(licence):
    pattern = r"^[A-Za-z]{2}\d{7}$|^[A-Za-z]{1}\d{6}$"
    if re.match(pattern, licence):
        return True
    else:
        return False

def isZipcodeValid(zip):
    pattern = r"^\d{4}[A-Za-z]{2}$"
    if re.match(pattern, zip):
        return True
    else:
        return False

def isPhoneNumberValid(phone):
    pattern = r"^\d{8}$"
    if re.match(pattern, phone):
        return True
    else:
        return False

def isSerialNumberValid(serial):
    pattern = r"^[a-zA-z0-9]{10,17}$"
    if re.match(pattern, serial):
        return True
    else:
        return False

def isDateValid(date):
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    if re.match(pattern, date):
        return True
    else:
        return False

def isUsernameValid(name):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_'.]{7,9}$"
    if re.match(pattern, name):
        return True
    else:
        return False