import json


def load_file():
    with open("passwords.json") as file:
        return json.load(file)


def save_file():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

passwords = load_file()

def add_password():
    site = input("enter the website: ").strip()
    usersname = input("enter the username: ").strip()
    words = input("enter your passwords: ").strip()
    manage = {
        "website" : site,
        "username" : usersname,
        "password" : words
    }
    passwords.append(manage)
    save_file()
    print("added successfully")


def dlet_password():
    while True:
        if not passwords:
            return
        show_password()
        item = input("enter the selceted item number:  ")
        if item.isdigit():
            item = int(item)
            if item in range(1, len(passwords) + 1):
                item = item - 1
                passwords.pop(item)
                save_file()
                print("dleted successfully")
                break
            else:
                print("insert anumber in range")
        else:
            print("insert the correct number")


def search_website():
    name = input("enter that name of the website").strip()
    found = False
    for password in passwords:
        if name == password["website"]:
            print(f"{password}")

            found = True
        if not found:
            print("no data related available")



 
def show_password():
    if not passwords:
        print("there is no data")
    else:
        for index, password in enumerate(passwords, start = 1):
            print("\n"
                f"{index}  -->>  "
                f"website = {password["website"]} || "
                f"username = {password["username"]} || "
                f"password = {password["password"]} || ")


def main():
    while True:
        print("------passwords manager------\n" "1.add passwords\n" "2.show passwords\n" "3.search website\n" "4.dlet password\n" "5.exit")
        choose = input("enter your response:")
        match choose:
            case "1":
                add_password()
            case "2":
                show_password()
            case "3":
                search_website()
            case "4":
                dlet_password()
            case "5":
                search_website()
            case "6":
                break
            case "7":
                print("insert a correct number")






main()