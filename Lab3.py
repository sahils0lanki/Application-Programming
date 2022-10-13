"""
Application Program:        Lab03.py
Programmer name:            Sahil Solanki
Dated:                      September 24th, 2022

This application enrolls a student in course and adds information about test mark1 and test mark2 in the course.
This application also calculates the average of the two tests for each student enrolled in the course.

"""
def add_student(student_info):
    first_name = input("Enter first name:\t")
    last_name = input("Enter last name:\t")
    student_number = input("Enter student number:\t")
    marks1 = input("Enter marks for test1:\t")
    marks2 = input("Enter marks for test2:\t")
    average_value = ((float(marks1) + float(marks2)) / 2)
    average = str ("%.2f" % average_value)

    data = ""
    if student_info == "":
        print("There are no students enrolled yet!")
        print("Student added in the list...")
        data += first_name+','+last_name+','+student_number+','+marks1+','+marks2+','+average
        student_info += data
        return student_info
    else:
        student_exist = False
        each_student_info = student_info.split(';')
        for student in each_student_info:
            student_details = student.split(',')
            if student_number == student_details[2]:
                print("Student number exists.")
                print("Student already enrolled.")
                print("Continue with correct information....")
                student_exist = True
                break
        if student_exist == False:
            print("Student added in the list...")
            data += first_name+','+last_name+','+student_number+','+marks1+','+marks2+','+average
            student_info += ';' + data
        return student_info

#Writing to display student information from the input written above
def display_student(student_info):
    if student_info == "":
        print("There are no students enrolled yet!")
    else:
        print("%50s" % "Displaying students data")
        print("%125s" % "Sahil Solanki")
        print("%125s" % "N01498358")
        display_student = ""
        header = ("%25s%25s%25s%15s%15s%20s\n" % ("First name","Last name","Student number","Mark 1","Mark 2","Average"))
        display_student += header
        each_student_info = student_info.split(';')
        for student in each_student_info:
            student_details = student.split(',')
            display = ("%25s%25s%25s%15s%15s%20s\n" % (student_details[0], student_details[1], student_details[2], student_details[3], student_details[4], student_details[5]))
            display_student += display
        print(display_student)

#main menu and options
def main_display():
    print("%60s" % "Student Registration Application")
    menu = """
    1. Add a student
    2. Display all students' information
    3. Search and Display student information
    4. End application 
    """

    print(menu)
    choice = input("Enter your choice now:\t")
    return choice

#searching students based on the student id
def search_student(student_info):
    if student_info == "":
        print("There is no student in records...")
    else:
        print("Choice is to search and display student information\n")
        search_student = input("Enter student number of student whose information is sought:\t")
        student_exist = False
        each_student_info = student_info.split(';')
        for student in each_student_info:
            student_details = student.split(',')
            if search_student == student_details[2]:
                print("Student is enrolled and is found in the list...")
                print("%60s" % "Displaying students data")
                print("%125s" % "Sahil Solanki")
                print("%125s" % "N01498358")
                header = ("%25s%25s%25s%15s%15s%20s\n" % ("First name", "Last name", "Student number", "Mark 1", "Mark 2","Average"))
                header += ("%25s%25s%25s%15s%15s%20s\n" % (student_details[0], student_details[1], student_details[2], student_details[3],student_details[4],student_details[5]))
                student_exist = True
                print(header)
                break
        if student_exist == False:
            print("This student is not enrolled yet! No information found...")
    return


def main():
    student_info = ""
    while True:
        choice = main_display()
        if choice == '1':
            student_info = add_student(student_info)
        elif choice == '2':
            display_student(student_info)
        elif choice == '3':
            search_student(student_info)
        elif choice == '4':
            print("Application now ending....")
            break
        else:
            print("Enter valid choice")


main()
