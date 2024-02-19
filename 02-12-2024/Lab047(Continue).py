# Continue

for num in range(1,10):
    print(num)

print("-----")

for num in range (1, 10):
    if num>1:
        print(num)

print("------")

for num in range(1, 10):  #  find the even num
    if num % 2 == 0:
        print(num)

print("-----")

for num in range(1,10):
    if num % 2 ==0:
        print(f"Found Even number{num}")  # f is here Formatting purpose
    else:
        print(f"Found ODD number{num}")

print("------")

for num in range (1,10):
    if num % 2 == 0:
        print(f"Found Even number {num}")
        continue
    print(f"Odd number{num}")