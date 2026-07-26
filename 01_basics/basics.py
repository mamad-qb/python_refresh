name = input("Enter your name: ")
height = int(input("Enter your height(cm): "))
height_meter = height / 100
age = int(input("Enter your age: "))
student = input("are you a student? (y or yes / n or no)").lower().strip()
if student in ("n", "no"):
    is_student = False
elif student in ("yes", "y"):
    is_student = True
else:
    is_student = False
    print("assuming not student")
city = input("Enter your hometown: ")
print(type(city), type(is_student), type(name))
print(f"my name is {name}, I am {age} years old, I am {height_meter:.2f} meters tall, I was born in {city} and my student_status is {is_student}")