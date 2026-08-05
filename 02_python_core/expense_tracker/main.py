# ==========================================
# Project: Expense Tracker (CLI)
# Author: Mohammad Ghorbanzadeh
# Repository: python_refresh
#
# Features:
# - Add expenses
# - Edit expenses
# - Delete expenses
# - Show all expenses
# - Calculate total expenses
# - Save data to JSON
# - Load data from JSON
#
# Concepts Practiced:
# - Functions
# - Lists & Dictionaries
# - Loops
# - Input Validation
# - File Handling
# - JSON Serialization
# - CRUD Operations
# ==========================================
import json


def load_file():
    with open ("expense.json", "r") as file:
        intery = []
        intery = json.load(file)
        return intery

def save_file():
    with open("expense.json", "w") as f:
        json.dump(expenses, f)



expenses = load_file()
CATEGORIES = ["food", "home", "car", "transportation", "cloth", "others"]

def get_amount():
    while True:
        money = input("enter the amount: ")
        if money.isdigit():
            money = abs(int(money))
            
            return money
        else:
            print("please insert a number")

def get_description():
    while True:
        desc = input("Enter the discription: ")
        if not desc:
            print("please insert a discription")
        else:
            return desc

def print_categories():
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
    amount = get_amount()

    print_categories()
    category = number_validation(CATEGORIES)

    description = get_description()

    expens = {
            "amount" : amount,
            "category" : CATEGORIES[(category - 1)],
            "description" : description
            }
    expenses.append(expens)
    save_file()
        

    print("expense added successfully")


def show_expenses():
    if not expenses:
        print("no expense added")
        return
    print(type(expenses))
    print(expenses)

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
        if not expenses:
            break
        else:
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
                                save_file()
                                print("changed successfully")
                                break
                            elif chosse == 2:
                                print_categories()
                                category = number_validation(CATEGORIES)
                                expenses[(edit - 1)]["category"] = CATEGORIES[(category - 1)]
                                print("changed successfully")
                                save_file()
                                break
                            elif chosse == 3:
                                descrip = input("enter the new description: ")
                                expenses[(edit - 1)]["description"] = descrip
                                print("changed successfully")
                                save_file()
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
            if int(dlet) in range (1, len(expenses) + 1):
                dlet = int(dlet)
                expenses.pop(dlet - 1)
                save_file()
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


