#Builder Pattern

class Pizza:
    def __init__(self,size:str, cheese:bool, toppings:list[str]):
        self.size=size
        self.cheese=cheese
        self.toppings=toppings

    def __str__(self):
        size_str=self.size + " sized Pizza, "
        cheese_str = "with cheese" if self.cheese else "with no cheese"
        toppings_str = ', '.join(self.toppings)+' toppings' if self.toppings else "no toppings"
        return size_str+cheese_str+' and ' +toppings_str
    

class PizzaBuilder:

    def __init__(self):
        self.size="medium"
        self.cheese=False
        self.toppings=[]
    
    def set_size(self, size:str):
        self.size=size
        return self
    
    def set_cheese(self, is_cheese:bool):
        self.cheese=is_cheese
        return self

    def set_toppings(self, toppings:list[str]):
        self.toppings=toppings
        return self
    
    def build(self): 
        return Pizza(self.size, self.cheese, self.toppings)
    

p1=(PizzaBuilder()
    .set_size('Large')
    .set_cheese(True)
    .set_toppings(['Anchovies','Onions'])
    .build())
print(p1)
p2=(PizzaBuilder()
    .set_size('Small')
    .set_cheese(False)
    .set_toppings(['tomatoes','Onions'])
    .build())
print(p2)
p3=(PizzaBuilder()
    .set_size('Large')
    .set_cheese(True)
    .set_toppings(['Anchovies','Onions'])
    .build())
print(p1 is p3)

    


"""
Builder Pattern Recap

📌 Why Builder?

Use when object creation has many optional parameters.

Instead of telescoping constructors (e.g., Pizza(size, cheese=True, toppings=[...])), we build step by step.

Why This is Good Design

✅ Avoids constructor overloads with too many params.
✅ Fluent interface → method chaining makes it readable.
✅ Extensible → easy to add new attributes like crust, sauce.
✅ Separates construction logic (builder) from the product (pizza).

6️⃣ Interview Explanation

If asked:

“I implemented the Builder pattern with a Pizza class representing the final product and a PizzaBuilder class that provides step-by-step methods (set_size, add_cheese, add_topping). The builder returns itself to allow method chaining. Finally, build() constructs the Pizza object. This design handles optional parameters cleanly, avoids large constructors, and makes object creation flexible and readable.”

PizzaDirector is simply a thing where we use it to define builder presets(here pizza builder presets) for different types of args initializations for the object creation



Where is Builder Pattern Used? (Cheat Sheet)

💡 Keep these practical examples in mind for interviews:

Object creation with many optional params:

Pizza ordering system 🍕

Burger customization 🍔

Resume/Profile builder 📝


Complex configuration objects:

HTTP Request builders (e.g., in Python’s requests.Request or Java’s HttpRequest.Builder)

SQL Query builders (SQLAlchemy, Hibernate Criteria API)

UI builders (Tkinter/React JSX-like patterns)


Game development:

Building characters with weapons, armor, skills

Serialization/Deserialization:

Building JSON objects gradually


Testing frameworks:

Fluent APIs for setting up test data (e.g., Mockito builders in Java)

👉 Interview trick: Always connect the pattern to real-life —

“We often use Builder when object construction has too many parameters. For example, query builders in ORMs or HTTP request builders in APIs are classic uses of this pattern.”
"""










