t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t))

# union ,means all the element
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


my_set = set1.union(set2)
print(my_set)

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
my_set2 = set2.difference(set1) 
print(my_set)
print(my_set2)