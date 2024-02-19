# Map()  --> function

def sq_of_number(num):
    return num**2

result = sq_of_number(10)
print(result)

numbers = [1, 2, 3, 4, 5]

# Map()
# 1. Takes Each item from the list
# 2. Execute the function on it
# 3. Return same number of elements ( list )


sq_numbers = list(map(sq_of_number, numbers))
print(sq_numbers)