import csv
import os.path
import hashlib

def createAccountDb(f = 'account.csv'):
    file_exists = os.path.exists(f)

    if (file_exists == False):
        with open(f, 'w', newline="") as account_file:
            fieldnames = ["user_name", "hashed_password", "user_type", "privilege_level", "ward_no"]
            csv.writer(account_file).writerow(fieldnames)

        print("Empty File Created Successfully")


def addNewAccount(user_name, password, user_type, privilege_level, ward_no):
    filename = 'account.csv'
    fieldnames = ["user_name", "hashed_password", "user_type", "privilege_level", "ward_no"]

    hs_pass = hashlib.md5(password.encode('utf-8'))
    encoded = hs_pass.digest()

    dict = {'user_name': user_name,
            'hashed_password': encoded,
            'user_type': user_type,
            'privilege_level': privilege_level,
            'ward_no': ward_no}

    with open(filename, 'a', newline="") as account_file:
        writer = csv.DictWriter(account_file, fieldnames=fieldnames)
        writer.writerow(dict)

def getNumberofLines(filename = "account.csv"):
    with open(filename) as f:
        return sum(1 for line in f)

def readItems():
    with open('account.csv', mode="r") as csv_file:  # "r" represents the read mode
        reader = csv.reader(csv_file)  # this is the reader object

        credentials = {}
        for item in reader:
            credentials[item[0]] = item[1:]
        credentials.pop("user_name")
        return  credentials

# addNewAccount("Admin", "admin", "Admin", 4, "None")