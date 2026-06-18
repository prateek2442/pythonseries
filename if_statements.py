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
