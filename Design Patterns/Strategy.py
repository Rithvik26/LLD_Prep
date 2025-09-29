#strategy pattern
from abc import ABC,abstractmethod
class PaymentStrategy(ABC):
    
    @abstractmethod
    def pay(self, amount:float): 
        pass

class UPIstrategy(PaymentStrategy):
    
    def __init__(self, id:str):
        self.upi_id=id
    
    def pay(self, amount:float):
        print("Payment done using upi id:",self.upi_id," of amount : ",amount)
    

class ApplePayStrategy(PaymentStrategy):
    
    def __init__(self, id:str):
        self.apple_id=id
    
    def pay(self, amount:float):
        print("Payment done using apple id:",self.apple_id," of amount : ",amount)


class PaymentProcessor:
    
    def __init__(self, strategy: PaymentStrategy):
        self.strategy=strategy
    
    def set_strategy(self, strategy): #this is for changing strategy at runtime
        self.strategy=strategy
    
    def make_payment(self, amount:float):
        self.strategy.pay(amount)
        
    

p1=PaymentProcessor(UPIstrategy('123'))

p1.make_payment(69)

p1.set_strategy(ApplePayStrategy('thanks66'))

        
p1.make_payment(44)


"""

📌 Definition:
Encapsulate algorithms/behaviors into separate classes, and make them interchangeable at runtime.

👉 Instead of writing if/else inside PaymentProcessor, we delegate to a Payment Strategy.


UML Diagram:
+-------------------+
| PaymentStrategy   |  <<interface>>
+-------------------+
| + pay(amount)     |
+-------------------+
       ^                 ^
       |                 |
+-----------------+   +----------------+
| UPIPayment      |   | WalletPayment  |
+-----------------+   +----------------+
| + pay(amount)   |   | + pay(amount)  |
+-----------------+   +----------------+

+-------------------------+
| PaymentProcessor        |
+-------------------------+
| - strategy: PaymentStrategy
+-------------------------+
| + set_strategy()        |
| + process_payment()     |
+-------------------------+



6️⃣ Why This is Good Design

✅ No if/else in PaymentProcessor → open for extension (new strategies).
✅ Interchangeable behaviors at runtime → flexible.
✅ Strategy Pattern cleanly separates context (PaymentProcessor) from algorithms (UPI, Wallet).
✅ Satisfies OCP from SOLID (adding new strategies without modifying context).

7️⃣ Interview Explanation

If asked:

“I implemented a PaymentStrategy interface with different concrete strategies like UPIPayment and WalletPayment. The PaymentProcessor class uses a strategy to process payments. I can change the strategy at runtime using set_strategy. This design follows the Strategy Pattern — making algorithms interchangeable, avoiding conditionals, and keeping the processor open for extension.”


 
"""
    
    
