# https://youtu.be/eiDyK_ofPPM?list=LL
#############################################################################################################################
"""
Cohesion and Coupling
"""
import random
import string

class VehicleRegistry:
    def generates_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        
    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.digits, k=2))}"

class Application:

    def register_vehicle(self, brand:str):
        registry = VehicleRegistry()
        vehicle_id = registry.generates_vehicle_id(12)
        vehicle_license_plate = registry.generate_vehicle_license(vehicle_id)

        price = 0
        if brand == "Tesla Model 3":
            price = 60000
        elif brand == "Volkswagen ID3":
            price = 35000
        elif brand == "BMW":
            price = 45000
        
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        payable_tax = price * tax_percentage

        print("Registration Complete")
        print(f"Brand: {brand}")
        print(f"Vehicle ID: {vehicle_id}")
        print(f"Vehicle License Plate: {vehicle_license_plate}")
        print(f"Payable Tax: {payable_tax}")

app = Application()
app.register_vehicle("Tesla Model 3")
#############################################################################################################################
"""
Cohesion and Coupling
"""
import random
import string

class VehicleInfo:
    brand: str
    price: float
    is_electric: bool

    def __init__(self, brand, is_electric, price):
        self.brand = brand
        self.is_electric = is_electric
        self.price = price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.is_electric:
            tax_percentage = 0.02
        return self.price * tax_percentage

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Vehicle ID: {self.id}")
        print(f"Vehicle License Plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, is_electric, price):
        self.vehicle_info[brand] = VehicleInfo(brand, is_electric, price)
    
    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW", False, 45000)

    def generates_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        
    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.digits, k=2))}"
    
    def create_vehicle(self, brand):
        vehicle_id = self.generates_vehicle_id(12)
        vehicle_license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, vehicle_license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand:str):
        registry = VehicleRegistry()
        # create a vehicle
        return registry.create_vehicle(brand)


app = Application()
vehe = app.register_vehicle("Tesla Model 3")
vehe.print()
#############################################################################################################################
