import random
import string

def ask_yes_or_no(question):
    """keep asking until the user enter the right answers"""
    while True:
        answer = input(question + " (yes/y orno/n):").lower().strip()
        if answer in ("yes", "y", "no", "n"):
            return answer
        else:
            print("invalid input, please follow instructure")




def generate_password():
        
    while True:
        length = input("enter your desirable lenght: ")
        correct = length.isdigit()
        if correct == True:
            length = int(length)
            break
        else:
            print("please insert a number.")



    use_uppercase = ask_yes_or_no("include uppercase letters?")
    use_number = ask_yes_or_no("include numbers?")
    use_symbols = ask_yes_or_no("include symbols?")


    selected_box = [string.ascii_lowercase]
    count = 1
    if use_number in ("yes", "y"):
        selected_box.append(string.digits)
        count += 1
    if use_symbols in ("yes", "y"):
        selected_box.append(string.punctuation)
        count += 1
    if use_uppercase in ("yes", "y"):
        selected_box.append(string.ascii_uppercase)
        count += 1

    if length < count:
        print("your conditions needs more letter to imply")
        quit()

    guarantee = []
    for char in selected_box:
        guarantee.append(random.choice(char))

    full_box = list(''.join(selected_box))

    remain = length - len(guarantee)
    random_Char = [random.choice(full_box) for _ in range(remain)]


    password_list = guarantee + random_Char
    random.shuffle(password_list)
    passwords = ''.join(password_list)
    return passwords

    

def check_strength(password):
    
    Score = 0
    if len(password) > 16:
        Score += 4
    elif len(password) > 12:
        Score += 2
    elif len(password) > 8:
        Score += 1

    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    Score += has_digit + has_lower + has_symbol + has_upper

    if Score > 7:
        strength = "Very Strong 💪"
    elif Score > 5:
        strength = "Strong ✅"
    elif Score > 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, Score



def main():
    password = generate_password()
    strength, score = check_strength(password)
    print(password)
    print(f"{strength} // score: {score}")


if __name__ == "__main__":
    main()

