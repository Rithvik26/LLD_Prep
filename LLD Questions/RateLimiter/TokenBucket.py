#RateLimiter 

#1.Token Bucket Algo

import time, threading

class TokenBucketRateLimiter:
    
    def __init__(self, capacity, token_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()
        self.token_rate = token_rate
        self._lock = threading.Lock()
        
    #we will refill the tokens if the tokens have been exhausted accoring to the token rate
    def refill(self):
        now = time.time()
        elapsed = now-self.last_refill
        tokens_to_add =int(elapsed * self.token_rate)
        
        if tokens_to_add>0:
            print(tokens_to_add, elapsed)
            self.tokens = min(self.tokens+tokens_to_add, self.capacity)
            self.last_refill = now
    
    def request(self):
        with self._lock:
            self.refill()
            if self.tokens>0:
                self.tokens-=1
                return True
            return False

TRL = TokenBucketRateLimiter(5,1)

for i in range(10):
    if TRL.request():
        print(f"Request number {i+1} has been successful!")
    else:
        print(f"Request number {i+1} has been Failed! RATE LIMITED")
    time.sleep(0.6)

        
    
""" 
The Token Bucket refills tokens at a fixed rate and allows bursts up to bucket capacity. 
Each request consumes a token; if no tokens are available, the request is denied.



I’d use a Token Bucket or Leaky Bucket algorithm.
Token Bucket refills tokens at a fixed rate and allows bursts up to bucket capacity. Each request consumes a token; if no tokens are available, the request is denied.
Leaky Bucket instead queues requests and processes them at a steady rate; if the queue is full, new requests are dropped.
In Python, I implemented Token Bucket with a refill method that calculates tokens based on elapsed time, and a thread lock for concurrency safety.


📝 Quick Interview Mapping

Token Bucket → best for APIs (allows bursts, then throttles).

Leaky Bucket → good for smoothing traffic (like network routers).

Both enforce rate limiting, but in slightly different ways.
"""
            
            
        