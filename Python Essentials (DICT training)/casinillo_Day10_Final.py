import random

db_name = "casinillo.txt"

class Reservation:
    def __init__(self, menuSelection):
        self.menuSelection = menuSelection

        if menuSelection == "V":                # View Reservation
            adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
            file = open(db_name, "r")
            report = ""
            i = 0

            for line in file:
                i += 1
                if i > 1:
                    stripped_line = line.strip()
                    line_list = stripped_line.split("\t\t\t")
                    adults += int(line_list[4])
                    children += int(line_list[5])
                    subtotalAdult = (int(line_list[4]) * 500)
                    subtotalChildren = (int(line_list[5]) * 300)
                    total += subtotalAdult + subtotalChildren
                    line_list.append(total)
                    report += f"{line_list[0]}\t\t\t{line_list[1]}\t\t\t{line_list[2]}\t\t\t" \
                              f"{line_list[3]}\t\t\t{line_list[4]}\t\t\t{line_list[5]}\t\t\t{line_list[6]}\n"

            file.close()

            print()
            print("CURRENT RESERVATIONS")
            print()
            print("#\t\t\tName\t\t\tDate\t\t\tTime\t\t\tAdults\t\tChildren\tTotal")
            print(report)

        elif menuSelection == "M":
            reservation_id = random.randint(0, 100)  # random number generator
            name = input("Enter Name: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")
            while True:
                try:
                    adults = int(input("No. of Adults: "))
                    children = int(input("No. of Children: "))
                    file = open(db_name, "a")
                    file.write(f"{reservation_id}\t\t\t{name}\t\t\t{date}\t\t\t{time}\t\t\t{adults}\t\t\t{children}\n")
                    file.close()
                    print()
                    break
                except ValueError:
                    print("Error: Invalid Input! Only numerical input is allowed.")
                    continue
        elif menuSelection == "D":
            reservation_id = input("Enter Reservation number: ")
            filedata1 = open(db_name, "r")
            lines = filedata1.readlines()
            filedata1.close()
            filedata2 = open(db_name, "w")

            for line in lines:
                if not line.startswith(reservation_id):
                    filedata2.write(line)
            filedata2.close()

        elif menuSelection == "G":
            adults, children, total_adults, total_children, total = 0, 0, 0, 0, 0
            file = open(db_name, "r")
            report = ""
            i = 0

            for line in file:
                i += 1
                if i > 1:
                    stripped_line = line.strip()
                    line_list = stripped_line.split("\t\t\t")
                    adults += int(line_list[4])
                    children += int(line_list[5])
                    subtotalAdult = (int(line_list[4]) * 500)
                    subtotalChildren = (int(line_list[5]) * 300)
                    total += subtotalAdult + subtotalChildren
                    line_list.append(subtotalAdult)
                    line_list.append(subtotalChildren)
                    line_list.append(total)
                    report += f"{line_list[0]}\t\t\t{line_list[1]}\t\t\t{line_list[2]}\t\t\t" \
                              f"{line_list[3]}\t\t\t{line_list[4]}\t\t\t{line_list[6]}\t\t{line_list[5]}\t\t\t" \
                              f"{line_list[7]}\t\t\t{line_list[8]}\n"
            file.close()

            print()
            print("REPORT")
            print()
            print("#\t\t\tName\t\t\tDate\t\t\tTime\t\t\tAdults\t\tSubtotal\tChildren\tSubtotal\tTotal")
            print(report)

        elif menuSelection == "E":
            exit("Thank you!")
        else:
            print("Invalid response. Please try again.")


while True:
    try:
        file = open(db_name, "r")
    except FileNotFoundError:
        file = open(db_name, "w+")
        file.write("#\t\t\tName\t\t\t        Date\t\t\t        Time\t\t\t    Adults\t\t\tChildren\n")
    file.close()

    print("Hotel Reservation System")
    print("V. View All Reservations\tM. Make Reservation")
    print("D. Delete Reservation\t\tG. Generate Report")
    print("E. Exit\n")

    menu = input('Enter selection [V, M, D, G, E]: ').upper()
    Reservation(menu)
