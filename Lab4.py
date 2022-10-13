def author_info():
    name = "%150s" % "Sahil Solanki"
    student_ID = "%150s\n" % "N01498358"
    print(name)
    print(student_ID)


def menu():
    menu = """
    1. Add Item in Inventory
    2. Display all items from inventory
    3. Inventory item sale
    4. End Application
    """
    print(menu)
    choice = input("Enter your choice:\t")
    return choice


item_inventory = []


def add_items(item_inventory):
    item = []
    i_name = input("Enter inventory item to add: \t ")
    i_sr_no = input("Enter item serial number: \t")
    i_qntity = ""
    i_price = float(input("Enter item price: \t"))

    while True:
        try:
            i_qntity = int(input("Enter item quantity: \t"))
            break

        except:
            print("Enter correct quantity of the item")
            continue

    if item_inventory == []:

        item.append(i_name)
        item.append(i_sr_no)
        item.append(i_qntity)
        item.append(i_price)
        item_inventory.append(item)


    else:
        print("There are items in the inventory... searching if the item name or serial number exists...")
        item_temp = 0

        for values in item_inventory:
            if values[1] == i_sr_no:
                print("Item Ser. No.: {} already exists in the inventory enter correct value".format(values[1]))
                values[2] += i_qntity
                item_temp = 1
                if values[3] < i_price:
                    values[3] = i_price
                break
        if item_temp == 0:
            item.append(i_name)
            item.append(i_sr_no)
            item.append(i_qntity)
            item.append(i_price)
            item_inventory = item_inventory.append(item)


def i_sell():
    sale_price = 0
    tax = 0
    amount = 0

    if item_inventory == []:
        print("There are no items in the inventory...")
    else:
        sale_menu = "1. Sale item by Name\n2. Sale item by serial number"
        print(sale_menu)
        sale_choice = input("Enter your choice:\t")

        if sale_choice == "1":
            sale_name = input("Enter the name of the item: \t")
            temp = 0
            for values in item_inventory:
                if values[0] == sale_name:
                    quantity = int(input("Enter quantity to sale: \t"))
                    temp = 1
                    if quantity > values[2]:
                        print("We do not have enough stock in quantity\n Sale does not go through...")
                    else:

                        sale_price = quantity * values[3]
                        tax = sale_price * 0.13
                        amount = sale_price * tax
                        values[2] -= quantity

                        ######### Print Bill###########

                        header = "%50s%50s%50s%50s\n" % ("Item Name", "Serial Number", "Item Quantity", "Item Price")
                        print(header)
                        ##    for values in item_inventory:
                        print_inventory = "%50s%50s%50s%50s\n" % (sale_name, values[1], quantity, values[3])
                        print(print_inventory)
                        # print(sale_price, amount, tax)
                        print_total = str("$" + str("%.2f" % (sale_price)))
                        print_total_amt = str("$" + str("%.2f" % (amount)))
                        print_tax = str("$" + str("%.2f" % (tax)))
                        print_bill = "%140s%10s\n%140s%10s\n%140s%10s" % (
                        "Total Sale Price -", print_total, "Tax Amount - ", print_tax, "Total Amount Paid - ",
                        print_total_amt)
                        print(print_bill)
                        return values[2]
                        break
            if temp == 0:
                print("Item not in stock")
        elif sale_choice == "2":
            temp = 0
            sale_serial_number = input("Enter the serial number of the item: \t")
            for values in item_inventory:
                if values[1] == sale_serial_number:
                    temp = 1
                    quantity = int(input("Enter quantity to sale: \t"))
                    if quantity > values[2]:
                        print("We do not have enough stock in quantity\n Sale does not go through...")
                    else:

                        print(item_inventory)
                        sale_price = quantity * values[3]
                        tax = sale_price * 0.13
                        amount = sale_price * tax
                        values[2] -= quantity

                        ######### Print Bill###########

                        header = "%50s%50s%50s%50s\n" % ("Item Name", "Serial Number", "Item Quantity", "Item Price")
                        print(header)
                        ##    for values in item_inventory:
                        print_inventory = "%50s%50s%50s%50s\n" % (values[0], sale_serial_number, quantity, values[3])
                        print(print_inventory)
                        # print(sale_price, amount, tax)
                        print_total = str("$" + str("%.2f" % (sale_price)))
                        print_total_amt = str("$" + str("%.2f" % (amount)))
                        print_tax = str("$" + str("%.2f" % (tax)))
                        print_bill = "%140s%10s\n%140s%10s\n%140s%10s" % (
                        "Total Sale Price -", print_total, "Tax Amount - ", print_tax, "Total Amount Paid - ",
                        print_total_amt)
                        print(print_bill)
                        return values[2]
                        break
            if temp == 0:
                print("Item not in stock")
        else:
            print("Please enter a Valid Choice:\t")
            i_sell()


def display():
    if item_inventory == []:
        print("There are no items in the inventory\n")
    else:
        author_info()
        header = "%50s%50s%50s%50s\n" % ("Item Name", "Serial Number", "Item Quantity", "Item Price")
        print(header)
        for values in item_inventory:
            print_inventory = "%50s%50s%50s%50s\n" % (values[0], values[1], values[2], values[3])
            print(print_inventory)


def main():
    while True:
        choice = menu()
        if choice == '1':
            add_items(item_inventory)
        elif choice == '2':
            display()
        elif choice == '3':
            i_sell()
        elif choice == '4':
            print("Ending Application...")
            exit()
        else:
            choice = input("Enter a Valid Choice: \t")


main()







