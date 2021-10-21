# abril jordan casinillo, Day9 Act2


print("\n++++++ Record Keeping App ++++++")
print("Select Operation: ")
print("A. Add Record ")
print("B. View Record ")
print("C. Clear Record ")
print("D. Exit app")


while True:

    menuSelection = input("\nSelect Operation [A, B, C, D]: ")

    if menuSelection.upper() in ("A", "B", "C", "D"):
        if menuSelection.upper() == "A":  # Add Record
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            file = open("record_keeping_app.txt", "a")
            file.write(f"{name}, {email}, {address}")
            file.close()
        elif menuSelection.upper() == "B":  # View Records
            print("Available Records: ")
            file = open("record_keeping_app.txt", "r")
            print(file.read())
            file.close()
        elif menuSelection.upper() == "C":  # Clear All Records
            print("No records found.")
            file = open("record_keeping_app.txt", "r+")
            file.truncate(0)
            file.close()
        elif menuSelection.upper() == "D":  # Exit app
            print("Thank you!")
            break
    else:
        print("Invalid Input")
