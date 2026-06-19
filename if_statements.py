#Exercise 1 - python calculator using if statement

operator = input("enter the operator (+ - * /):")

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1+num2
    print(result)

elif operator == "*":
    result = num1*num2
    print(result)

elif operator == "/":
    result = num1/num2
    print(result)

else:
    print("Operator not supported")


#Exercise 2 - python weight converter

weight = float(input("enter your weight:"))
unit = input("kilogram or pound ? : (K or L)")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight in kilogram is, {weight} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight in pound is, {weight} {unit}")

else:
    print("Operator not supported")

