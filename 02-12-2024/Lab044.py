# Break
# For -> 1 to 10 -> range (1,11,1), range (1,11)
# i = 5 -> break from the loop - kicked out from the loop

for counter in range(0,11):
    if counter == 5:
        break   # kicking out from loop
    print(counter)
print("Outside of the loop")


for counter in range (3,15):
    if counter == 7: 
        break
    print(counter)
print("outside of the loop")