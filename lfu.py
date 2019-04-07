import heapq

from threading import Lock


class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        # the number of times this bad boy was fetched
        self.count = 1

    def __lt__(self, o):
        return self.count > o.count

    def __repr__(self):
        return f'{self.val}:{self.count}'


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

    def get(self, k):
        # get is not much work
        node = self.lookup.get(k)

        # if not node, then just return null
        if not node:
            return None

        # o/w get the node and update the count
        with self.mutex:
            node.count += 1

            # and heapify the remains
            heapq.heapify(self.q)

        # and return the value
        return node.val

    def put(self, k, v):
        with self.mutex:
            # if exists then a mere update
            if k in self.lookup:
                self.lookup[k].val = v
                return

            # if cap is reached, then get the guy out
            if len(self.q) == self.cap:
                # then remove an element
                popped = self.q.pop()
                # heapify
                heapq.heapify(self.q)
                # also remove from the lookup
                if popped.key not in self.lookup:
                    raise RuntimeError('what!!')
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
    assert(cache.get(4) is None)
    # pass print
    print("passed test")
