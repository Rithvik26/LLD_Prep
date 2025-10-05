#LeakyBucket Rate Limiter

import time, threading
from collections import deque
class LeakyBucketRateLimiter:
    
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leaks_queue=deque()
        self.leak_rate = leak_rate
        self._lock = threading.Lock()
        self.last_leak = time.time()
    
    def refill(self):
        now = time.time()
        elapsed = now - self.last_leak
        leaks = int(elapsed * self.leak_rate)
        m=len(self.leaks_queue)
        if leaks>0:
            for i in range(min(leaks, m)):
                self.leaks_queue.popleft()
            self.last_leak = now
    
    def request(self, request):
        
        with self._lock:
            self.refill()
            if len(self.leaks_queue)<self.capacity:
                self.leaks_queue.append(request)
                return True
            return False

LB = LeakyBucketRateLimiter(5, 1)

for i in range(10):
    if LB.request(i):
        print(f"The request {i+1} has been sucessfull!")
    else:
        print(f"The request {i+1} has been Failed! [RATE LIMITED]")
    time.sleep(0.4)
                

""" 
Leaky Bucket queues incoming requests and processes them at a steady rate(leak rate); if the queue is full, new requests are dropped.

"""