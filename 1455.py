students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        students.append([name, roll])
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("-------------------------")
            for student in students:
                print("Name :", student[0], " Roll No :", student[1])

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        found = False

        for student in students:
            if student[1] == roll:
                print("Student Found")
                print("Name :", student[0])
                print("Roll No :", student[1])
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")