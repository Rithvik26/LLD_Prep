#Observer Pattern
from abc import ABC, abstractmethod

#Observer
class Observer(ABC):
    
    @abstractmethod
    def update(self):
        pass

class User(Observer):
    
    def __init__(self,id):
        self.user_id=id
        
    
    def update(self, message:str):
        print("the user",self.user_id,"has been notified with message:",message)
    

#Publisher
class NotificationService:
    def __init__(self):
        self.observers=[]
   
    def add_observer(self,observer: Observer):
        self.observers.append(observer)
    
    
    def remove_observer(self,observer: Observer):
        self.observers.remove(observer)
    
    def notify_all(self,message):
        for ob in self.observers:
            ob.update(message)
    
    def event_change(self, message):
        self.notify_all(message)

user1=User("1")
user2=User("2")

service=NotificationService()

service.add_observer(user1)
service.add_observer(user2)

service.event_change("messi scored a goal")

service.remove_observer(user2)

service.event_change("ronaldo scored a goal")





    
    
"""  
Definition:

Defines a one-to-many dependency between objects.

When the subject changes, all observers are notified automatically.


-Why This is Good Design

✅ Loosely coupled → NotificationService doesn’t care who the users are, it just notifies observers.
✅ Extensible → can add new observer types (e.g., EmailUser, SMSUser) without touching NotificationService.
✅ Real-world fit → used in GUIs, event-driven systems, pub-sub messaging (Kafka, RabbitMQ).

7️⃣ Interview Explanation

If asked:

“I implemented the Observer pattern with NotificationService as the Subject and User as Observer. Users subscribe (attach) or unsubscribe (detach) from the service. Whenever a new event happens, the service calls notify_all(), which in turn calls each observer’s update(). This design decouples event producers from event consumers and matches real-world notification systems, chat apps, or stock price tickers.”
"""