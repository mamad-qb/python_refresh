
expenses = []
CATEGORIES = ["food", "home", "car", "transportation", "cloth", "others"]


def print_categpry():
        for index, cat  in enumerate(CATEGORIES, start = 1):
            print(f"{index}. {cat}")


def number_validation(ITEMM):
    while True:
        x = input("Enter your selected number: ")
        if x.isdigit():
            x = int(x)
            if x in range(1, len(ITEMM)+ 1):
                return x
                break
            else:
                print("insert a number in the given range")
        else:
            print("insert the number")    


def add_expenses():
    print("\n Add new expense") 
    while True:
        amount = input("Enter the amount")
        if amount.isdigit():
            amount = int(abs(amount))
            break
        else:
            print("insert a number")

    while True:
        print_categpry()
        category = number_validation(CATEGORIES)

        description = input("enter description: ")

        expens = {
            "amount" : int(amount),
            "category" : CATEGORIES[(category - 1)],
            "description" : description
            }

        expenses.append(expens)

        print("expense added successfully")
        break


def show_expenses():
    if not expenses:
        print("no expense added")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f" {expense["amount"]} |"
            f" {expense["category"]} |"
            f" {expense["description"]} |"
        )


def show_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"total is {total}")

def edit_expense():
    show_expenses()
    while True:
        edit = number_validation(expenses)
        print(
                    "\nselect the topic"
                    "\n1. amount" \
                    "\n2. category"
                    "\n3. description"
                )
        while True:
                    chosse = input("select the item number: ")
                    if chosse.isdigit():
                        chosse = int(chosse)
                        if chosse in (1, 2, 3):
                            if chosse == 1:
                                amount = int(input("enter the new amount: "))
                                expenses[(edit - 1)]["amount"] = amount
                                print("changed successfully")
                                break
                            elif chosse == 2:
                                print_categpry()
                                category = number_validation(CATEGORIES)
                                expenses[(edit - 1)]["category"] = CATEGORIES[category]
                                print("changed successfully")
                                break
                            elif chosse == 3:
                                descrip = input("enter the new description: ")
                                expenses[(edit - 1)]["description"] = descrip
                                print("changed successfully")
                                break
                        else:
                            print("insert the correct number")
                    else:
                        print("insert a digit")

        break


def dlet_data():
    show_expenses()
    if not expenses:
        return 0
    while True:
        dlet = input("enter the number: ")
        if dlet.isdigit():
            print(len(expenses))
            if int(dlet) in range (1, len(expenses) + 1):
                dlet = int(dlet)
                expenses.pop(dlet - 1)
                print("dleted successfully")
                break
            else:
                print("insert a exact object number")
        else:
            print("insert a digit")
while True:
    print("\n ---expense tracker---")
    print("1. add expense")
    print("2. dlet expence")
    print("3. show expense")
    print("4. show total")
    print("5. edit expenses")
    print("6. exit")

    choice = input("choose: ")

    match choice:
        case "1":
            add_expenses()
        case "2":
            dlet_data()
        case "3":
            show_expenses()
        case "4":
            show_total()
        case "5":
            edit_expense()
        case "6":
            print("byebye")
            break
        case _:
            print("invalid input")


