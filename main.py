import hashlib
import os.path
import config
import account
import records

def checkConfig():
    account.createAccountDb()
    records.createAccountDb()

    file_exists = os.path.exists("config.ini")
    if(file_exists):
        user_config_credentials = config.readConfig()
        # print(user_config_credentials)

        all_credentials_dict = account.readItems()
        # print(all_credentials_dict)

        userName = user_config_credentials["user_name"]
        hashedPassword = user_config_credentials["hashed_password"]

        if((userName in all_credentials_dict) and (hashedPassword == all_credentials_dict[userName][0])):
            userType = all_credentials_dict[userName][1]
            priviledgeLevel = all_credentials_dict[userName][2]
            wardNo = all_credentials_dict[userName][3]

            print("Welcome 1")
            return {"user_name": userName,
                    "hashed_password": hashedPassword,
                    "user_type": userType,
                    "privilege_level": priviledgeLevel,
                    "ward_no": wardNo}
        else:
            return None
    else:
        return None

def logIn():
    res = checkConfig()
    if res == None:
        userName = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        hs_pass = hashlib.md5(password.encode('utf-8'))
        encoded = hs_pass.digest()

        all_credentials_dict = account.readItems()

        if ((userName in all_credentials_dict) and (str(encoded) == all_credentials_dict[userName][0])):
            userType = all_credentials_dict[userName][1]
            priviledgeLevel = all_credentials_dict[userName][2]
            wardNo = all_credentials_dict[userName][3]

            print("Welcome!")
            return {"user_name": userName,
                    "hashed_password": str(encoded),
                    "user_type": userType,
                    "privilege_level": priviledgeLevel,
                    "ward_no": wardNo}
        else:
            print("User credentials are invalid")
            return None
    else:
        return res

def doctorPriviledges(wardNo):
    print("To add new record input 1, To view medical records input 2")
    option = int(input("Select option: ").strip())

    if option == 1:
        #create medical record
        date = input("Enter Date: ").strip()
        patient_name = input("Enter Patient Name: ").strip()
        age = input("Enter Age: ").strip()
        sickness_details = input("Enter Sickness Details: ").strip()
        drug_prescriptions = input("Enter Drug Prescriptions: ").strip()
        lab_test_prescriptions = input("Enter Lab Test Prescriptions: ").strip()

        records.addNewRecord(date,
                 patient_name,
                 age,
                 wardNo,
                 sickness_details,
                 drug_prescriptions,
                 lab_test_prescriptions)
        print("Record successfully added!!")
    elif option == 2:
        #view records
        records.getPatientRecordbyWardNo(wardNo)
    else:
        print('Invalid Input')

def nursePriviledges(wardNo):
    print("Do you want to view patient records? (Y/N)")
    option = input("Select option: ").strip()
    if(option == "Y" or option == "y"):
        records.getPatientRecordbyWardNo(wardNo)
    else:
        print("Thank you for using the system!")

def labPriviledges():
    print("Do you want to view patient lab prescriptions? (Y/N)")
    option = input("Select option: ").strip()
    if (option == "Y" or option == "y"):
        records.getLabPrescriptions()
    else:
        print("Thank you for using the system!")

def patientPriviledges(patientName):
    print("Do you want to view medical records of yours? (Y/N)")
    option = input("Select option: ").strip()
    if (option == "Y" or option == "y"):
        records.getPatientRecordsbyPatientName(patientName)
    else:
        print("Thank you for using the system!")


userDetails = logIn()
if userDetails != None:
    if userDetails['user_type'] == 'Doctor' and userDetails['privilege_level'] == '3':
        doctorPriviledges(userDetails['ward_no'])
    elif userDetails['user_type'] == 'Nurse' and userDetails['privilege_level'] == '2':
        nursePriviledges(userDetails['ward_no'])
    elif userDetails['user_type'] == 'Lab' and userDetails['privilege_level'] == '1':
        labPriviledges()
    elif userDetails['user_type'] == 'Patient' and userDetails['privilege_level'] == '0':
        patientPriviledges(userDetails['user_name'])
    else:
        print("ERROR")
