"""
Application Program:        Lab 1
Programmer name:            Sahil Solanki
Dated:                      September 9, 2022

This application takes five positive numbers, determines the average value and standard deviation.

"""
def my_function():
    display = "%90s\n" % ("Sahil Solanki")
    display += "%90s\n" % ("N01498358")

    first_number = (float(input("Enter first number:\t")))
    second_number = (float(input("Enter second number:\t")))
    third_number = (float(input("Enter third number:\t")))
    fourth_number = (float(input("Enter fourth number:\t")))
    fifth_number = (float(input("Enter fifth number:\t")))

    add = first_number + second_number + third_number + fourth_number + fifth_number
    avg = add / 5

    std = ((first_number - avg) ** 2 + (second_number - avg) ** 2 + (third_number - avg) ** 2 + (
                fourth_number - avg) ** 2 + (fifth_number - avg) ** 2)
    std1 = "%.2f" % (std)
    std2 = float(std1) / 5
    std3 = (std2) ** 0.5

    heading = "%0s%15s%15s%15s%15s%15s%30s\n" % (
    "First Value", "Second Value", "Third Value", "Fourth Value", "Fifth Value", "Average", "Standard Deviation")
    #print(display)
    #print(heading)

    value1 = str("%.2f" % (first_number))
    value2 = str("%.2f" % (second_number))
    value3 = str("%.2f" % (third_number))
    value4 = str("%.2f" % (fourth_number))
    value5 = str("%.2f" % (fifth_number))
    avgfinal = str("%.2f" % (avg))
    stdfinal = str("%.2f" % (std3))

    final = display + heading + "%0s%15s%15s%15s%15s%19s%19s"%(value1, value2, value3, value4, value5, avgfinal, stdfinal)
    print(final)

my_function()
