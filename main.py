import hashlib
import os.path
import config
import account
import records

#check config file exist
def checkConfig():
    account.createAccountDb()
    records.createMedicalRecordsDb()

    file_exists = os.path.exists("config.ini")
    if(file_exists):
        user_config_credentials = config.readConfig()
        all_credentials_dict = account.readUserDetails()

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

#Log in functionality of the system
def logIn():
    res = checkConfig()
    if res == None:
        userName = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        hs_pass = hashlib.md5(password.encode('utf-8'))
        encoded = hs_pass.digest()

        all_credentials_dict = account.readUserDetails()

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

# Adding new Medical Record and View medical records functions handling
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

# View Patient Records by ward No handling
def nursePriviledges(wardNo):
    print("Do you want to view patient records? (Y/N)")
    option = input("Select option: ").strip()
    if(option == "Y" or option == "y"):
        records.getPatientRecordbyWardNo(wardNo)
    else:
        print("Thank you for using the system!")

#view lab prescription records functionality handling
def labPriviledges():
    print("Do you want to view patient lab prescriptions? (Y/N)")
    option = input("Select option: ").strip()
    if (option == "Y" or option == "y"):
        records.getLabPrescriptions()
    else:
        print("Thank you for using the system!")

#View patient Records assigned to a specific patient functionality handling
def patientPriviledges(patientName):
    print("Do you want to view medical records of yours? (Y/N)")
    option = input("Select option: ").strip()
    if (option == "Y" or option == "y"):
        records.getPatientRecordsbyPatientName(patientName)
    else:
        print("Thank you for using the system!")

#add new user to the system and view all medical records functionality handling
def adminPrivileges():
    print("To add new user input 1, To view medical records input 2, To view all users input 3")
    option = int(input("Select option: ").strip())

    if option == 1:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        user_type = input("Enter User Type (Hospital_Staff OR Patient): ").strip()
        privilege_level = input("Enter Privilege level (0, 1, 2 ,OR 3): ").strip()
        ward_no = input("Enter Ward No: ").strip()

        if(user_type not in ["Hospital_Staff", "Patient"]):
            print("Invalid user type!")
        elif(privilege_level not in ["0", "1", "2", "3"]):
            print("Invalid privilege level!")
        elif((user_type == "Patient") and (privilege_level in ["1", "2", "3"])):
            print("Invalid privilege level for a Patient!")
        elif ((user_type == "Hospital_Staff") and (privilege_level == "0")):
            print("Invalid privilege level for a Hospital staff member!")
        else:
            account.addNewAccount(username, password, user_type, privilege_level, ward_no)

    elif option == 2:
        records.getAllPAtientRecords()
    elif option == 3:
        account.getAllUsers()
    else:
        print("Thank you for using the system!")

userDetails = logIn()
if userDetails != None:
    if userDetails['user_type'] == 'Admin' and userDetails['privilege_level'] == '4':
        adminPrivileges()
    elif userDetails['user_type'] == 'Hospital_Staff' and userDetails['privilege_level'] == '3':
        doctorPriviledges(userDetails['ward_no'])
    elif userDetails['user_type'] == 'Hospital_Staff' and userDetails['privilege_level'] == '2':
        nursePriviledges(userDetails['ward_no'])
    elif userDetails['user_type'] == 'Hospital_Staff' and userDetails['privilege_level'] == '1':
        labPriviledges()
    elif userDetails['user_type'] == 'Patient' and userDetails['privilege_level'] == '0':
        patientPriviledges(userDetails['user_name'])
    else:
        print("ERROR")
