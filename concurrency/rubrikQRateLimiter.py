"""
Design a rate limiter
QPS: Queries Per Second
set_qps
accept

Question:
1.1 .. 1.59 .. (1000) 2:01 (window sliding)
1.1    2.0 (700) 2.1 1000

concurrency .. ?
"""

from collections import deque
from threading import RLock
import time

class RateLimiter:
    def __init__(self, qps):
        "qps -> QPS that is defined"
        self.qps = qps
        self.requests = deque()
        self.lock = RLock()
        
        assert self.qps > 0, "QPS cannot be negative"

    def accept(self):
        with self.lock:
            # get the timestamp val for this request
            ts = time.time() * 1000
            # evict all the entries which are expired
            self.evict(ts)
            # if length is still equal to qps, then false ...
            if len(self.requests) >= self.qps:
                return False
            else:
                self.requests.append(ts)
            return True
            
    # accept -> evict
    def evict(self, ts):
        # peek
        with self.lock:
            # come back equals or not
            while len(self.requests) > 0 and self.requests[0] < ts - 1000:
                self.requests.popleft()

                
def test():
    ratelimiter = RateLimiter(10)
    
    for i in range(110):
        print(f'request {i} got accepted? {ratelimiter.accept()}')
        time.sleep(0.01)

test()

	
