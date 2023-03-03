"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage 
instance attributes
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Vehicle(100, 10)
print(car1.max_speed, car1.mileage)

"""
OOP Exercise 4: Class Inheritance
Given:
Create a Bus class that inherits from the Vehicle class. Give the capacity 
argument of Bus.seating_capacity() a default value of 50.
"""
class Vehicle:
    def __init__(self, name , max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The Seating capacity of a {self.name} is {capacity}"
class Bus(Vehicle):
    # def __init__(self, name, max_speed, mileage):
    #     super().__init__(name, max_speed, mileage)
    def seating_capacity(self, capacity = 100):
        return super().seating_capacity(capacity)

B = Bus("School Bus", 100, 10)
print(f"{B.seating_capacity()}")

