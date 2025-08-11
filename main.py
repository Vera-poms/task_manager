# Ask user to input the length of the 3 sides of a trianglr
x = float(input("Enter the first side: "))
y = float(input("Enter the second side: "))
z = float(input("Enter the third side: "))
# If all sides are equal print Equilateral
# If 2 sides are equal print Isosceles
# If no sides are equal print Scalene

if x == y and y == z:
    print("Equilateral")
elif x == y or y == z or x == z:
    print("Isosceles")
else:
    print("Scalene")
