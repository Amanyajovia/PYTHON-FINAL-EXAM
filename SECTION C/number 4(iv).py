
class Car:
    def __init__(self, brand,name, color):
        self.brand = brand
        self.name = name  
        self.color = color 
         

my_car = Car("Benz", "Mercedes","Blue")

print(f"Brand: {my_car.brand}")
print(f"Name: {my_car.name}")
print(f"Color: {my_car.color}")