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
    response = input("\nDo you want to enlist a subject? (yes/no/exit): ")
    if response == 'yes':
        print("Enlisting a subject.")
        print("Available Subjects:")
        print(avSubject)

        while True:
            enlistingSubject = input("Enter the subject name you want to enlist: or type 'exit' to quit ): ").strip()
            if enlistingSubject == "exit":
                
                break
            if enlistingSubject.lower() not in avSubject['subjectName'].str.lower().values:
                print("Invalid subject name. Please enter a valid subject from the available subjects list.")
                
                continue

            if enlistingSubject in enlistedSubject['subjectName'].values:
                print("Subject already enlisted. Please choose a different subject.")
                
                continue
                            
            row = avSubject[avSubject['subjectName'].str.lower() == enlistingSubject.lower()].iloc[0]
            new_day = row['day']
            new_start = row['startTime']
            new_end = row['endTime']

            conflict = False

            for i in range(len(enlistedSubject)):
                if new_day == enlistedSubject.loc[i, 'day']:
                    if new_start < enlistedSubject.loc[i, 'endTime'] and enlistedSubject.loc[i, 'startTime'] < new_end:
                        print("Time conflict detected with an already enlisted subject.")
                        conflict = True
                        break

            if conflict:
                continue
            break
        
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
                enlistedSubject.to_csv("data/enlistedSubject.csv", index=False)
                print("Saved changes to CSV file.")
                break
            


            elif commit == 'no':
                print("Changes not committed.")
                selected_row = None
                break

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        
        continue
        
        
    if response == 'no' and response == 'exit':    
        print("Exiting the program.")
        selected_row = None
        break 

    
    else:
        print("Invalid input. Please enter 'yes' to continue or 'no' or 'exit' to quit.")
        selected_row = None
        break
    
print("enlisted subjects:")
print(enlistedSubject)


