#Exercise 1 -  calculate area of rectangle

length = float(input("Enter the length of the string: "))#we use float() to convert the data type of the length
breadth = float(input("Enter the breadth of the string: "))

area = length * breadth

print("the area of the rectangle is ", area)



#Exercise 2 - create to program to know what a person has bought and how many and calculate the total amount

item = input("which item would u like to buy :")
price = float(input("Enter the price of the item: "))
quantity = float(input("Enter the quantity of the item: "))

Total_price = price * quantity

print("the total price of your purchase is ", Total_price)



#Exercise 3 - create a program for madlib game
print("Today i tried to make a 3D ________ .")
print("Then i ________ of eating something _________")
print("After that i ________ with my friends.")


blank1 = input("fill the first blank:")
blank2 = input("fill the second blank:")
blank3 = input("fill the third blank:")
blank4 = input("fill the fourth blank:")

print(f"Today i tried to make a 3D {blank1} .")
print(f"Then i {blank2} of eating something {blank3}.")
print(f"After that i {blank4} with my friends.")