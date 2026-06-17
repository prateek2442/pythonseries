#Exercise 1 - circumference of a circle using math library

import math

radius = float(input("Enter the radius of the circle:"))

circumference = 2 * math.pi * radius

print(f"the circumference of the circle is : {round(circumference, 2)}")



#Exercise 2 - Area of the circle using math library

import math

radius_sec_circle =  float(input("Enter the radius of the circle : "))

area = math.pi * pow(radius_sec_circle, 2)

print(f"The area of the circe is : {round(area, 2)}")


#Exercise 3 - calculate Hypotenuse of a right triangle using math lib

import math

A = float(input("Enter the length of A : "))
B = float(input("Enter the length of B : "))

c = math.sqrt(pow(A, 2) + pow(B, 2))

print(f"The hypotenuse C after calculating using A and B is : {round(c, 2)}")
