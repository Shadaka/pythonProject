api_response = {
    "first_name": "Shadaka",
    "age": 34,
    "last_name": "Islam",
    "email": "shadaka.islam@gmail.com",
    "password": "Test@123",
    "Commission": 10
}

print(api_response)
print(type(api_response))                    # Dict - is immutable, it can change the value
print(api_response.get("password"))

api_response["password"] = "Shadaka"
print(api_response.get('password'))

for key, value in api_response.items():
    print(key, " => ", value)