#ParkingLot

""" 
Entities: Vehicle, ParkingSlot, Strategy pattern: SlotAssignmentStrategy, NearestSlotStrategy, ParkingLot(singleton)
"""

from abc import ABC, abstractmethod
import threading
#Vehicle

class Vehicle:
    def __init__(self, number: str, vehicle_type: str): 
        self.vehicle_type = vehicle_type
        self.number = number
    
    def drive(self):
        print(f"The vehicle {self.vehicle_type} with registration number {self.number} is driving")
    

#ParkingSlot

class ParkingSlot:
    def __init__(self, slot_id: int, level: int, vehicle_type: str):
        self.slot_id=slot_id
        self.level=level
        self.vehicle_type=vehicle_type
        self.vehicle=None
        self.isFree=True
    
    def park(self, vehicle: Vehicle):
        if self.isFree and self.vehicle_type==vehicle.vehicle_type:
            self.vehicle=vehicle
            self.isFree=False
            return True
        return False
    
    def leave(self, vehicle: Vehicle):
        self.vehicle=None
        self.isFree=True
    

#SlotAssignmentStrategy

class SlotAssignmentStrategy(ABC):
    
    @abstractmethod
    def findslot(self,slots: list[ParkingSlot], vehicle: Vehicle):
        pass


class NearestSlotStrategy(SlotAssignmentStrategy):
    
    def findslot(self, slots: list[ParkingSlot], vehicle: Vehicle):
        
        for slot in slots:
            if slot.isFree and slot.vehicle_type==vehicle.vehicle_type:
                return slot
        
        return None


#ParkingLot

class ParkingLot:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ParkingLot, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, levels, spots_per_level):
        
        # Avoid reinitialization in Singleton
        if not hasattr(self, "initialized"):
            self.slotstrategy=NearestSlotStrategy()
            self.slots=[]
            for level in range(levels):
                for slot in range(spots_per_level):
                    if slot%2==0:
                        self.slots.append(ParkingSlot(slot, level, "car"))
                    else:
                        self.slots.append(ParkingSlot(slot, level, "bike"))

    
    def set_strategy(self, strategy: SlotAssignmentStrategy):
        self.slotstrategy=strategy
    
    def park_vehicle(self, vehicle: Vehicle):
        slot=self.slotstrategy.findslot(self.slots, vehicle)

        if slot:
            if slot.park(vehicle):
                print(f"The {vehicle.vehicle_type} vehicle with [ID]: {vehicle.number} has been parked at [LEVEL]:{slot.level} and slot number:{slot.slot_id}")
                
        
        else:
            print("No slots available")
    
    def leave_vehicle(self, vehicle: Vehicle):
        
        for slot in self.slots:
            if slot.vehicle==vehicle:
                slot.leave(vehicle)


car=Vehicle("8898","car")
car2=Vehicle("MKV57","car")
P=ParkingLot(3,5)

P.park_vehicle(car)
P.park_vehicle(car2)


"""
PARKING LOT.

Interview-ready Script

“I’ll design the Parking Lot with four main entities: Vehicle, ParkingSpot, ParkingLot, and Strategy for spot assignment.
Vehicles can be Cars or Bikes. Spots know their type and whether they’re free. The ParkingLot is a Singleton so only one instance manages the whole system.
For extensibility, I use the Strategy Pattern for assigning spots — today it’s nearest, tomorrow it could be cheapest or random.
When a vehicle enters, ParkingLot asks the strategy for the best available spot, parks the vehicle, and marks the spot as occupied. On exit, the spot is freed.
This design is modular, follows SOLID principles, and can be extended to add payments, tickets, or display boards without changing existing code.”


UML Diagram:

Vehicle 
number: int
vehicle_type: str
-----------------
drive()

[CAR]    [BIKE]
(factory in future)


Parkingslot
slot_id: int
level: int
vehicle_type: str
vehicle: Vehicle
isFree: bool
-----------------
park(vehicle)
leave(vehicle)


SlotAssignmentStrategy(ABC)
find_slot(vehicle) ->abstractmethod
       
NearestSlotAssignment(SlotAssignmentStrategy)
find_slot(vehicle)
.
.


ParkingLot
slots: list[Parkingslot]
levels: int
slots_per_level: int
slotstrategy: SlotAssignmentStrategy
-------------------------------------
set_strategy(strategy: SlotAssignmentStrategy)
park_vehicle(vehicle: Vehicle)
leave_vehicle(vehicle: Vehicle)








"""


        
            
                    
            
                
            
            
        
                
        
            
         

