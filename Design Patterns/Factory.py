#Factory Pattern

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bike(Vehicle):
    def drive(self):
        print("Driving a bike")
    

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type.lower()=='car':
            return Car()
        elif vehicle_type.lower()=='bike':
            return Bike()
        else:
            return 'invalid vehicle type'
    

car=VehicleFactory().create_vehicle('Car')
car.drive()


"""

For the Factory, I defined an abstract Vehicle and concrete Car and Bike. 

A VehicleFactory class creates instances based on type. 

This hides object creation logic and makes the design extensible. 

These are classic creational patterns: Singleton ensures controlled global access, 
and Factory centralizes object creation.

3️⃣ Why this is Good Design

✅ Factory centralizes object creation → caller just asks for "car" or "bike", doesn’t worry about constructors.
✅ Both follow SOLID:

Singleton helps resource management.

Factory supports OCP (easy to add Truck without touching client code).



Note:If singleton + factory used in vehiclefactory example:
In Python, I used the __new__ method to enforce Singleton. __new__ is called before __init__, and I store the single instance in a class variable _instance. 
If an instance already exists, __new__ returns it instead of creating a new one. This guarantees that all references point to the same object. 
To prevent re-initialization, I used an initialized flag in __init__. I also extended this to a VehicleFactory Singleton — ensuring a single shared factory that creates vehicles. 
This shows both Singleton and Factory working together.
"""



#Abstract Factory Pattern
# Abstract Factories
"""
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Vehicle:
        pass
    
    @abstractmethod
    def create_bike(self) -> Vehicle:
        pass


# Concrete Factories
class PetrolVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car()  # Petrol Car
    def create_bike(self) -> Vehicle:
        return Bike()  # Petrol Bike


class ElectricVehicleFactory(VehicleFactory):
    def create_car(self) -> Vehicle:
        return Car()  # Electric Car (different implementation in real case)
    def create_bike(self) -> Vehicle:
        return Bike()  # Electric Bike
factory = ElectricVehicleFactory()
car = factory.create_car()
bike = factory.create_bike()

car.drive()
bike.drive()
"""

""" 

Interview Answer

If asked:

“What’s the difference between Factory and Abstract Factory?”

You say:

“Factory Method deals with creating objects of a single hierarchy — for example, Car or Bike from VehicleFactory.
Abstract Factory is a higher-level pattern that creates families of related objects. For example, an ElectricVehicleFactory and a PetrolVehicleFactory might each produce both cars and bikes, but they belong to the same respectivefamily. 
Factory = single product, Abstract Factory = related product families.”
"""