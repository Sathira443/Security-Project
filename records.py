import os.path
import csv

# create medical records database
def createMedicalRecordsDb(f='medical_records.csv'):
    file_exists = os.path.exists(f)

    if (file_exists == False):
        with open(f, 'w', newline="") as record_file:
            fieldnames = ["date",
                          "patient_name",
                          "age",
                          "sickness_details",
                          "drug_prescriptions",
                          "lab_test_prescriptions"]
            csv.writer(record_file).writerow(fieldnames)

        print("Empty File Created Successfully")


# add new medical record entry
def addNewRecord(date,
                 patient_name,
                 age,
                 ward,
                 sickness_details,
                 drug_prescriptions,
                 lab_test_prescriptions):
    filename = 'medical_records.csv'
    fieldnames = ["date",
                  "patient_name",
                  "age",
                  "ward",
                  "sickness_details",
                  "drug_prescriptions",
                  "lab_test_prescriptions"]

    dict = {'date': date,
            'patient_name': patient_name,
            'age': age,
            'ward': ward,
            'sickness_details': sickness_details,
            'drug_prescriptions': drug_prescriptions,
            'lab_test_prescriptions': lab_test_prescriptions,
            }

    with open(filename, 'a', newline="") as record_file:
        writer = csv.DictWriter(record_file, fieldnames=fieldnames)
        writer.writerow(dict)


# Returns list of Patient Records using a Ward No
def getPatientRecordbyWardNo(ward_no):
    filename = 'medical_records.csv'
    with open(filename, 'r') as record_file:
        reader = csv.reader(record_file)
        for item in reader:
            if item[3] == ward_no:
                print("\nDate :" + item[0])
                print("Patient Name: " + item[1])
                print("Age: " + item[2])
                print("Sickness Details: " + item[4])
                print("Drug Prescriptions: " + item[5])
                print("Lab Test Prescriptions: " + item[6])


# Returns list of lab prescriptions
def getLabPrescriptions():
    filename = 'medical_records.csv'
    with open(filename, 'r') as record_file:
        reader = csv.reader(record_file)

        for item in reader:
            if ((item[6] != "None") and (item[6] != "lab_test_prescriptions")):
                print("\nDate :" + item[0])
                print("Patient Name: " + item[1])
                print("Age: " + item[2])
                print("Lab Test Prescriptions: " + item[6])


# Returns list of Patient Records by Patient name
def getPatientRecordsbyPatientName(patientName):
    filename = 'medical_records.csv'
    with open(filename, 'r') as record_file:
        reader = csv.reader(record_file)

        for item in reader:
            if (item[1] == patientName):
                print("\nDate :" + item[0])
                print("Age: " + item[2])
                print("Ward No: " + item[3])
                print("Sickness Details: " + item[4])
                print("Drug Prescriptions: " + item[5])
                print("Lab Test Prescriptions: " + item[6])

#get all patient records
def getAllPAtientRecords():
    filename = 'medical_records.csv'
    with open(filename, 'r') as record_file:
        reader = csv.reader(record_file)

        for item in reader:
            if (item[6] != "lab_test_prescriptions"):
                print("\nDate :" + item[0])
                print("Patient Name: " + item[1])
                print("Age: " + item[2])
                print("Ward No: " + item[3])
                print("Sickness Details: " + item[4])
                print("Drug Prescriptions: " + item[5])
                print("Lab Test Prescriptions: " + item[6])