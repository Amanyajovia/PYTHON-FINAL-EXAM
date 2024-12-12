class Car:
    def __init__(self, brand,name, color):
        self.brand = brand
        self.name = name  
        self.color = color
    def start_engine(self):
        print(f"The engine of the {self.name} {self.brand} and {self.color}  in color has started.")


my_car = Car("Benz","Mercedes" "Black")
my_car.start_engine()