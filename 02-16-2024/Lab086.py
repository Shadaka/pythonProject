# Dict
# kay and value
name = "Shadaka"

#key -> name
# value -> "name"
# A Dictionary is an unorderes collection of data
# ina a key-value pair forma

my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))

phone_book = {"Batman" : 2434114, "Superman":67641461981, "Wonder WOmen":6471346193844 }
print(len(phone_book))
print(phone_book["Batman"])
print(phone_book["Superman"])

phone_book2 = dict(batman=123, Cersei=342, GB=323)
print(phone_book2)
print(phone_book2["GB"])
print(phone_book2['GB'])
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

shadaka_details = dict(name="shadaka", age=40, isMail=True, Address="Austin")
shadaka_details2 = {"name":"shadaka", "90":40, "isMail":True, "Address":"Austin"}
print(shadaka_details2.get(90))

my_dict = {'a': 1, 'b ': 2, 'c' : 3, 'a': 95}
print(len(my_dict))
print(my_dict)