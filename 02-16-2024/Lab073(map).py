import math   # map is created for list of item

def sq_rt(num):
    return math.sqrt(num)
    # return math.cbrt(num) cbrt means cube root

my_list = [21, 34, 54]
sq_list = list(map(sq_rt, my_list))
print(sq_list)