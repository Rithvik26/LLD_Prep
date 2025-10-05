#Elevator LLD - using state pattern

from abc import ABC, abstractmethod

class ElevatorState(ABC):
    @abstractmethod
    def request_floor(self, elevator, floor_number):
        pass
    @abstractmethod
    def arrive(self, elevator):
        pass

#Elevator has states - idle,Moving up, moving down, maintenance

class IdleState(ElevatorState):
    
    def request_floor(self, elevator, floor_number):
        if elevator.current_floor==floor_number:
            print(f"You are already at the floor {floor_number}")
        
            
        elif elevator.current_floor<floor_number:
            elevator.set_state(MovingUpState())
        else:
            elevator.set_state(MovingDownState())
        elevator.target_floor = floor_number
    
    def arrive(self, elevator):
        print(f"You are at the Idle state, Please press any floor number to go to it")


class MovingUpState(ElevatorState):
    
    def request_floor(self, elevator, floor_number):
        
        elevator.target_floor=floor_number
    
    def arrive(self, elevator):
        elevator.current_floor+=1
        print(f"Elevator at floor {elevator.current_floor}")
        if elevator.current_floor==elevator.target_floor:
            print(f"You have arrived at your floor {elevator.target_floor}")
            elevator.set_state(IdleState())



class MovingDownState(ElevatorState):
    
    def request_floor(self, elevator, floor_number):
        elevator.target_floor=floor_number
    
    def arrive(self, elevator):
        elevator.current_floor-=1
        print(f"Elevator at floor {elevator.current_floor}")
        
        if elevator.current_floor==elevator.target_floor:
            print(f"You have arrived at your floor {elevator.target_floor}")
            elevator.set_state(IdleState())


class MaintenanceState(ElevatorState):
    
    def request_floor(self, elevator, floor_number):
        print(f"The elevator is on maintenance! Please come again")
    
    def arrive(self, elevator):
        print(f"The elevator is on maintenance! Please come again")


class Elevator:
    
    def __init__(self):
        self.current_floor=0
        self.target_floor=0
        self.state= IdleState()
    
    def set_state(self, state: ElevatorState):
        self.state=state
    
    def request_floor(self, floor_number):
        self.state.request_floor(self, floor_number)
    
    def step(self):
        self.state.arrive(self)



elevator=Elevator()

elevator.request_floor(3)

for _ in range(4):
    elevator.step()

elevator.request_floor(0)

for _ in range(4):
    elevator.step()


        
        
        
""" 
How State Pattern helps here:

Instead of writing:

if state == "Idle": ...
elif state == "MovingUp": ...


… we encapsulate each state’s behavior into its own class.

The Elevator (context) delegates to the current state object.

When state changes (Idle → MovingUp → Idle), behavior changes automatically.

Answer template in interview:

“I modeled the elevator using State Pattern. Each state (Idle, MovingUp, MovingDown, Maintenance) implements the same interface but defines different behavior for request_floor() and arrive(). The Elevator itself delegates behavior to its current state, so when I switch states, the behavior changes without messy if-else conditions. This makes the design clean, extensible, and easy to maintain.”
"""