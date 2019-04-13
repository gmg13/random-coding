# 
# Your previous Java content is preserved below:
# 
# 

# windowed map .. windows size is fixed!
# streams .. timestamp (current)
# 

from datetime import datetime
from datetime import timedelta
from queue import Queue
from threading import Lock

class Node:
    def __init__(self, k, v, ts):
        self.k = k
        self.v = v
        self.ts = ts


class WindowedMap:
    def __init__(self, wsize):
        self.wsize = wsize
        # initiate the DS
        # k -> Node
        self.lookup = {} # hash map .. k, v anything
        # 
        self.wobjects = [] # this is linked list .. both ends .. queue
        self.wsum = 0
        # locking mech
        self.lock = Lock()

    def _remove_marked_ones(self):
        """actively removing expiring objects from the dataset"""
        with self.lock:
            while True:
                if not self.wobjects:
                    return
                expired = self.is_expired(self.wobjects[0])
                if not expired:
                    return
                # atomically
                obj = self.wobjects.pop(0)
                del self.lookup[obj.k]
                # ...
                self.wsum -= obj.v
            
    def is_expired(self, n):
        return datetime.now() - timedelta(hour=self.wsize) > n.ts

    def get(self, k):
        # all i have to do is fetch
        if k not in self.lookup:
            return None
        n = self.lookup[k]
        # 
        if datetime.now() - timedelta(hour=self.wsize) < n.ts:
            return n.v
        # 
        self._remove_marked_ones()

        return None

    def put(self, k, v):
        # just to make sure that window size is in check
        self._remove_marked_ones()

        # k is not there
        if k not in self.lookup:
            n = Node(k, v, datetime.now())
            self.wobject.append(n)
            self.lookup[k] = n
            # update the sum
            self.wsum += v
        else:
            n = self.lookup[k]
            # remove the element from the list
            self.wobjects.remove(n)
            # add the current timestamp to the object
            n.ts = datetime.now()
            # hdl sum
            self.wsum += (v - n.v) 
            # value
            n.v = v
            # append it the list
            self.wobjects.append(n)

    def avg(self):
        # just to make sure that window size is in check
        self._remove_marked_ones()

        # compute the average and return
        # bug
        if not len(self.wobjects):
            return 0.0
        # ...
        return self.wsum * 1.0 / len(self.wobjects)


def test():
    # (k1, v1, 10); (k2, v2, 120) get@5, get@90 get@130
    # (k1, v1, 50); (k1, v2, 100) get@180
    pass
