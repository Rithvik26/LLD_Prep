#decorator pattern
from abc import ABC, abstractmethod
import random
import time


# Step 1: APIClient Interface
class APIClient(ABC):
    @abstractmethod
    def request(self, url: str) -> str:
        pass


# Step 2: Concrete Implementation
class BaseAPIClient(APIClient):
    def request(self, url: str) -> str:
        # Simulate random failure
        if random.choice([True, False]):
            raise Exception("Network error!")
        return f"Response from URL:{url}"


# Step 3: Abstract Decorator
class APIClientDecorator(APIClient):
    def __init__(self, client: APIClient):
        self._client = client

    def request(self, url: str) -> str:
        return self._client.request(url)


# Step 4: Logging Decorator
class LoggingAPIClient(APIClientDecorator):
    def request(self, url: str) -> str:
        print(f"[LOG] Sending request to {url}")
        result = super().request(url)
        print(f"[LOG] Received response: {result}")
        return result


# Step 5: Retry Decorator
class RetryAPIClient(APIClientDecorator):
    def __init__(self, client: APIClient, retries: int = 3, delay: float = 1.0):
        super().__init__(client)
        self.retries = retries
        self.delay = delay

    def request(self, url: str) -> str:
        for attempt in range(1, self.retries + 1):
            try:
                return super().request(url)
            except Exception as e:
                print(f"[RETRY] Attempt {attempt} failed: {e}")
                if attempt < self.retries:
                    time.sleep(self.delay)
        raise Exception(f"Failed after {self.retries} retries")

#Step 6: Caching Decorator
class CacheAPICLient(APIClientDecorator):
    def __init__(self, client):
        super().__init__(client)
        self.cache={}
    
    def request(self, url: str) ->str:
        if url in self.cache:
            print("the response is from the cache")
            response= self.cache[url]
            return response
        response=super().request(url)
        self.cache[url]=response
        return response

client=BaseAPIClient()
client=LoggingAPIClient(client)
client=RetryAPIClient(client,3,0.5)
client=CacheAPICLient(client)


try:
    resp=client.request("request 1")
    print("the response is", resp)
    
    print("retrying with same url and seeing if it came form cache")
    resp=client.request("request 1")
    print("the response is", resp)
    
except Exception as e:
    print("Request Failed:",e)

""" 
Why This is Good Design

✅ Decorator Pattern → we added logging + retry without modifying BaseAPIClient.
✅ Open/Closed Principle → extend functionality without changing existing code.
✅ Flexible composition → we can mix decorators (Retry + Logging, or Logging only).
✅ Real-world relevance → API clients often need cross-cutting concerns like logging, retries, caching, authentication.

7️⃣ Interview Explanation

If asked:

“I designed an APIClient interface and a BaseAPIClient. To add extra behaviors like logging and retries, 
I wrapped the base client in decorators LoggingAPIClient and RetryAPIClient. 
These decorators implement the same interface, so they can be composed flexibly. This avoids subclass explosion and respects OCP. A real-world analogy is middleware in HTTP clients — we add logging, retry, or caching layers dynamically without touching the base client.”



1️⃣ Are all SOLID principles used here?

Yes ✅ — your decorator example demonstrates almost every SOLID principle:

S — Single Responsibility Principle (SRP)

Each decorator has one job:

LoggingAPIClient → logging

RetryAPIClient → retries

CacheAPIClient → caching

No God class mixing all responsibilities.

O — Open/Closed Principle (OCP)

You can add new decorators (e.g., AuthAPIClient, RateLimitAPIClient) without modifying existing code.

Your BaseAPIClient doesn’t change → it’s closed for modification but open for extension via decorators.

L — Liskov Substitution Principle (LSP)

Every decorator is still an APIClient.

That means you can pass LoggingAPIClient, RetryAPIClient, or CacheAPIClient anywhere a normal APIClient is expected.

✅ Substitutability holds true.

I — Interface Segregation Principle (ISP)

APIClient interface has just one method: request().

Clients aren’t forced to implement unnecessary methods.

✅ Keeps interfaces lean and focused.

D — Dependency Inversion Principle (DIP)

APIClientDecorator depends on the abstraction APIClient, not the concrete BaseAPIClient.

High-level logic (Retry, Logging, Cache) is decoupled from the low-level implementation (network call).

📌 Conclusion: Yes, your decorator stack (Logging + Retry + Cache) is a textbook demonstration of SOLID.
"""
    

            
    
