#Singleton
class ConnectionPool:
    _instance=None
    _connections=[]

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance=super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self,"initialized"):
            self._connections=[]
            self.max_connections=3
        
    def add_conn(self):
        if len(self._connections)<self.max_connections:
            self._connections.append(len(self._connections)+1)
            return True
        return None
    
    def remove_conn(self,conn):
        if conn in self._connections:
            self._connections.remove(conn)
            return True
        else:
            return "Not Found"

cp1=ConnectionPool()
cp2=ConnectionPool()
print(cp1 is cp2)

"""

✅ Singleton ensures only one ConnectionPool exists → prevents resource over-allocation.
For the Singleton, I overrode __new__ to ensure only one instance of ConnectionPool exists, and managed a simple pool of connections.

1️⃣ How __new__ Enforces Singleton
In Python, object creation happens in two steps:
__new__ → actually creates the instance (low-level allocation).
__init__ → initializes attributes of that instance.
So if we want only one object, we control it inside __new__.

First time: _instance is None → creates an object via super().__new__.

Later calls: _instance already exists → returns the same reference instead of making a new one.

"""




