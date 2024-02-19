# Filter
# it can filter the items from the list based on the tragic
# return less number of items

number = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = filter(lambda x:x%2 == 0, number)
#even_numbers = filter(lambda num:num%2 == 0, number)
#even_numbers = filter(lambda item:item%2 == 0, number)


def even(num):
    return num%2 == 0
even_lambda = lambda num:num % 2 == 0

even_numbers = filter(even, number)

print(list(even_numbers))

