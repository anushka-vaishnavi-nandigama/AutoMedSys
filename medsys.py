import csv
import os
if not os.path.exists('health_reports.csv'):
    with open('health_reports.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Patient ID", "Patient Name", "Diagnosis", "Date"])
def ar(patient_id, patient_name, diagnosis, date):
    with open('health_reports.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, patient_name, diagnosis, date])
    print(f"New report added for {patient_name}.")
def sr(patient_id):
    with open('health_reports.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        found = False
        for row in reader:
            if row[0] == patient_id:
                found = True
                print(f"ID: {row[0]}, Name: {row[1]}, Diagnosis: {row[2]}, Date: {row[3]}")
        if not found:
            print(f"No reports found for ID: {patient_id}")
while True:
    print("1: Add a new health report")
    print("2: View existing reports")
    print("3: Exit the system")
    user_choice = input("Select an option: ")
    if user_choice == '1':
        patient_id = input("Enter Patient ID: ")
        patient_name = input("Enter Patient Name: ")
        diagnosis = input("Enter Diagnosis: ")
        date = input("Enter Date: ")
        ar(patient_id, patient_name, diagnosis, date)
    elif user_choice == '2':
        patient_id = input("Enter Patient ID to search for: ")
        sr(patient_id)
    elif user_choice == '3':
        break 
    else:
        print("Invalid choice. Please select a valid option.")
