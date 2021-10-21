# abril jordan casinillo, Day9 Act3
import random
import fileinput

print("++++++ Record Keeping App ++++++")
print("Select Operation: ")
print("A. Add Record ")
print("B. View Records ")
print("C. Edit Email ")
print("D. Clear All Records ")
print("E. Exit")

while True:

    menuSelection = input("\nSelect Operation [A, B, C, D , E]: ")

    if menuSelection.upper() in ("A", "B", "C", "D", "E"):
        if menuSelection.upper() == "A":  # Add Record
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            reservation_id = random.randint(0, 10)
            file = open("record_keeping_app.txt", "a")
            file.write(f"\n{reservation_id}, {name}, {email}, {address}")
            file.close()
        elif menuSelection.upper() == "B":  # View Records
            file = open("record_keeping_app.txt", "r")
            print("Available Records: ")
            print(file.read())
            file.close()
        elif menuSelection.upper() == "C":  # Edit Email
            old_email = input("Edit Old email: ")
            new_email = input("New email: ")
            file = open("record_keeping_app.txt", "r")
            filedata = file.read()
            file.close()
            newdata = filedata.replace(old_email, new_email)
            file = open("record_keeping_app.txt", 'w')
            file.write(newdata)
            file.close()
        elif menuSelection.upper() == "D":  # Clear All Records
            print("No records found.")
            file = open("record_keeping_app.txt", "r+")
            file.truncate(0)
            file.close()
        elif menuSelection.upper() == "E":  # Exit
            print("Thank you!")
            exit()
    else:
        print("Invalid Input")