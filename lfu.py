import heapq

from threading import Lock
from time import time


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        # the number of times this bad boy was fetched
        self.count = 1
        self.ts = time()

    def __lt__(self, o):
        if self.count == o.count:
            return self.ts < o.ts
        return self.count < o.count

    def __repr__(self):
        return f'{self.val}:{self.count}:{self.ts}'


class LFUCache:
    def __init__(self, cap=10):
        # capacity and what not
        self.cap = cap
        # the data structs to use to store the data!
        self.q = []
        self.lookup = {}  # can be map with size for efficiency
        # mutex
        self.mutex = Lock()

    def __repr__(self):
        return str([self.lookup, self.q])

    def clear(self):
        with self.mutex:
            self.lookup.clear()
            self.q = []

    def get(self, k):
        # get is not much work
        node = self.lookup.get(k)

        # if not node, then just return null
        if not node:
            return -1

        # o/w get the node and update the count
        with self.mutex:
            node.count += 1
            node.ts = time()

            # and heapify the remains
            heapq.heapify(self.q)

        # and return the value
        return node.val

    def put(self, k, v):
        if not self.cap:
            return

        with self.mutex:
            # if exists then a mere update
            if k in self.lookup:
                self.lookup[k].val = v
                # increase the freq
                self.lookup[k].count += 1
                self.lookup[k].ts = time()
                # heapify the best
                heapq.heapify(self.q)
                # and return
                return

            # if cap is reached, then get the guy out
            if len(self.q) == self.cap:
                # then remove an element
                popped = heapq.heappop(self.q)
                # heapify
                heapq.heapify(self.q)
                # also remove from the lookup
                del self.lookup[popped.key]

            # add the node and to the party
            n = Node(k, v)
            # add to the lookup
            self.lookup[k] = n
            # append to the q
            self.q.append(n)
            # heapify the remains
            heapq.heapify(self.q)


def test():
    cache = LFUCache(4)
    # insert a three elements twice and one once
    cache.put(1, '1')
    cache.put(2, '2')
    cache.put(3, '3')
    cache.put(4, '4')
    # and get three elements to up their count
    cache.get(1)
    cache.get(2)
    cache.get(3)

    # now try inserting a 5
    cache.put(5, '5')
    # this should have removed the 4
    assert(cache.get(4) == -1)

    # clear everything
    del cache
    cache = LFUCache(2)

    # another test case
    # create a cache with capacity 2
    # insert 2, then 1, then update 2.
    # then insert 4, should remove 1
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    # now insert 4
    cache.put(4, 1)
    # and try get 1 first and then try and get 2
    assert(cache.get(1) == -1)
    assert(cache.get(2) == 3)

    # another test case
    # ["LFUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    # [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
    # expected [null,null,null,null,null,4,3,2,-1,null,-1,2,3,-1,5]

    # pass print
    del cache
    cache = LFUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    # import pdb; pdb.set_trace()
    # print(cache)
    cache.put(4, 4)
    # print(cache)
    assert(cache.get(4) == 4)
    assert(cache.get(3) == 3)
    assert(cache.get(2) == 2)
    assert(cache.get(1) == -1)
    cache.put(5, 5)
    assert(cache.get(1) == -1)
    assert(cache.get(2) == 2)
    assert(cache.get(3) == 3)
    assert(cache.get(4) == -1)
    assert(cache.get(5) == 5)
    print("everything passed successfully!!")
