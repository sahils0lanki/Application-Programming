"""
Application Program:        Lab 2
Programmer name:            Sahil Solanki
Dated:                      September 19, 2022

This application validates email domain address for every registered customer and
displays information in formatted output.
"""
def my_function():
    menu = """
        1. Enter first name, last name and email address
        2. Display complete customer information, registered so far
        3. End Application
    """
    first_name = ""
    last_name = ""
    email = ""


    display = "%120s" % ("Sahil Solanki\n")
    display += "%119s" % ("N01498358\n")
    display += "%75s" % ("Sahil Solanki Corporation\n")
    display += "%20s%45s%60s"%("First Name", "Last Name","Email Contact Information\n")



    while True:
        print(menu)
        my_choice = input("Enter your choice:\t")
        if my_choice == '1':
            first_name = input("Enter first name:\t")
            last_name = input("Enter last name:\t")
            email = input("Enter customer email contact address:\t")
            domain ="@sahil.ca"

            for count in range(3):
                if email[-9:] == domain:
                    display += "%20s%45s%59s\n"%(first_name, last_name, email)
                    break
                else:
                    email=input("Please try again:\t")


        elif my_choice == '2':
            if first_name == "" + last_name == "" + email == "":
                print("There are no customers registered to the organization")
            else:
                print(display)


        elif my_choice == '3':
            print("Thanks. Bye!")
            break

        else:
            print("Please enter valid number:\t")

my_function()