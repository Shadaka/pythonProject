class bike:
    color = None
    model = None

    def bike_details(self):
        print("My bike details is",  self.color, self.model)

bike_color = input("Enter your bike color is \n")
bike_model = input("Enter your bike model is \n")

bike_obj_ref = bike()
bike_obj_ref.color = bike_color
bike_obj_ref.model = bike_model

bike_obj_ref.bike_details()
