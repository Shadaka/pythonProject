# Triangle Cla
# Side1 == Side2 == SIde3 --> Equal
# side1 == side ==2 or side2 == side3 or side1 == side3 ---->Isolated

side1 = float(input("Enter the side 1\n"))
side2 = float(input("Enter the side 2\n"))
side3 = float(input("Enter the side 3\n"))

if side1 == side2 == side3:
    print("Equal")
elif side1 == side2 or side1 == side3 or side1 == side3:
    print("Isolation")
else:
    print("Scalene")
    