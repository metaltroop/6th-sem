import csv

student_fields = ['Roll', 'Name', 'Age', 'Email', 'Phone']
student_database = 'students.csv'

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    student_data = [input(f"Enter {field}: ") for field in student_fields]

    with open(student_database, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(student_data)
    print("Data saved successfully")
    input("Press Enter to continue")

def view_students():
    print("--- Student Records ---")
    with open(student_database, "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for i, field in enumerate(student_fields):
            print(f"{field:<15}", end='')
        print("\n-----------------------------------------------------------------")
        for row in reader:
            for item in row:
                print(f"{item:<15}", end='')
            print("\n")
    input("Press Enter to continue")

def search_student():
    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and roll == row[0]:
                print("----- Student Found -----")
                for field, value in zip(student_fields, row):
                    print(f"{field}: {value}")
                break
        else:
            print("Roll No. not found in our database")
    input("Press Enter to continue")

def update_student():
    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    updated_data = []
    with open(student_database, "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and roll == row[0]:
                print("Student Found:")
                student_data = [input(f"Enter {field}: ") for field in student_fields]
                updated_data.append(student_data)
            else:
                updated_data.append(row)
    with open(student_database, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    print("Data updated successfully")
    input("Press Enter to continue")

def delete_student():
    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    updated_data = []
    student_found = False  # Add a flag to check if the student is found
    with open(student_database, "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and roll == row[0]:
                print(f"Roll no. {roll} deleted successfully")
                student_found = True
            else:
                updated_data.append(row)
    if not student_found:  # Check if the student was not found
        print("Roll No. not found in our database")
    with open(student_database, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    input("Press Enter to continue")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    print("-------------------------------")
    print(" Thank you for using our system")
    print("-------------------------------")

if __name__ == "__main__":
    main()
