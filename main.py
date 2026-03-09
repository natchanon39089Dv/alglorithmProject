import numpy as np
import pandas as pd





#starting the program

avSubject = pd.read_csv("data/availableSubjectList.csv")
enlistedSubject = pd.read_csv("data/enlistedSubject.csv")

print("Available Subjects:")
print(avSubject)

print("\nEnlisted Subjects:")
print(enlistedSubject)


def addSubject(enlistedSubject, subjectName, credits, time, day, startTime, endTime, lecturer, subjectCode):
    new_subject = {
        "subjectName": subjectName,
        "credits": credits,
        "time": time,
        "day": day,
        "startTime": startTime,
        "endTime": endTime,
        "lecturer": lecturer,
        "subjectCode": subjectCode
    }

    enlistedSubject.loc[len(enlistedSubject)] = new_subject
    print(f"Added {subjectName} to enlisted subjects.")
    return enlistedSubject

#loop
while True:
    response = input("\nDo you want to enlist a subject? (yes/no): ").strip().lower()
    if response == 'yes':
        print("Enlisting a subject.")
        print("Available Subjects:")
        print(avSubject)
        
        enlistingSubject = input("Enter the subject name you want to enlist: ").strip()
        while True:
            if enlistingSubject.lower() in avSubject['subjectName'].str.lower().values:
                break
            else:
                print("Invalid subject name. Please enter a valid subject from the available subjects list.")
                enlistingSubject = input("Enter the subject name you want to enlist: ").strip()
        
        
        selected_row = avSubject[avSubject['subjectName'].str.lower() == enlistingSubject.lower()].iloc[0]

        
        
        
        selected_row = avSubject[avSubject['subjectName'].str.lower() == enlistingSubject.lower()].iloc[0]

        print(f"Selected subject: {selected_row['subjectName']}")

        while True:
            commit = input("commit changes? (yes/no): ").strip().lower()

            if commit == 'yes':
                enlistedSubject = addSubject(
                    enlistedSubject,
                    selected_row['subjectName'],
                    selected_row['credits'],
                    selected_row['time'],
                    selected_row['day'],
                    selected_row['startTime'],
                    selected_row['endTime'],
                    selected_row['lecturer'],
                    selected_row['subjectCode']
                )
                break

            elif commit == 'no':
                print("Changes not committed.")
                break

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        
        
        
        
        
    else:
        print("Exiting the program.")
        break 
    
print("enlisted subjects:")
print(enlistedSubject)


