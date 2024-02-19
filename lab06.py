#age = 23
#phone_number = 12322
#isMarried = True
#isTupurMarried = False

#sequence
#name = "Tupur"
#name1 = "Aydin"

#print("name1")

#a, b, c = 12, True, "tupur"
#print(a, b, c)

name = input("Enter Name:")
print(name)
age = input("Enter age:")
print(age)
roll_number = input("Enter roll number:")
print(roll_number)
phone_number = input("Enter phone number:")
print(phone_number)




num = int(input("Enter the number of table which you want:"))
print("Table of ", num, "is")
for i in range(1,11):
    print(num, "*", i, "=", (i*num))