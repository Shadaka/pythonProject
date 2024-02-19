# Tuple = Collection of items

# Lit = Collection of items, List are mutable in nature

# List are mutable, it can be change
# Tuple are mutable


# Tuple

my_list = [1,2,3,4,5,61,17]


print(my_list)
print(type(my_list))
print(len(my_list))

my_tuple = (1, 2, 3, 4, 5, 7, 8, 9,)

print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

# convert list to tuple
new_tuple = tuple(my_list)
print(new_tuple)