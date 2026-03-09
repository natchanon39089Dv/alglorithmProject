import numpy as np
import pandas as pd





#starting the program

avSubject = pd.read_csv("data/availableSubjectList.csv")
enlistedSubject = pd.read_csv("data/enlistedSubject.csv")
#withdraw system

print("\nEnlisted Subjects:")
print(enlistedSubject)
print("\nWithdraw System")

while True:
    if len(enlistedSubject) == 0:
        print("No subjects to withdraw.")
        break

    print("\nEnlisted Subjects:")
    print(enlistedSubject[['subjectName','day','startTime','endTime']])

    subject = input("Enter subject name to withdraw (or type 'exit'): ").strip()

    if subject.lower() == "exit":
        break

    if subject.lower() not in enlistedSubject['subjectName'].str.lower().values:
        print("Subject not found in enlisted list.")
        continue

    # find row
    row_index = enlistedSubject[
        enlistedSubject['subjectName'].str.lower() == subject.lower()
    ].index

    enlistedSubject = enlistedSubject.drop(row_index)

    print(f"{subject} withdrawn successfully.")

    # reset index
    enlistedSubject = enlistedSubject.reset_index(drop=True)

    # save file
    enlistedSubject.to_csv("data/enlistedSubject.csv", index=False)

    print("Updated enlisted subjects saved.")