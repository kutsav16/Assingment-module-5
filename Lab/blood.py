# Program: Check if a person is eligible to donate blood using nested if

age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood.")
else:
    print("You are not eligible to donate blood.")
