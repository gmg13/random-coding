# my meagre attempt to crack the first round of confl*
# there are a few new things like printabout decorator for
# basic debugging
# there is something wrong here. particularly eviction
# strategy, but I leaving it as that because this was
# what i did under pressure

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

# Qs
# 1. get(k) .
# 2. limits ... int(8) .. >= 1
# k1; k2; get(k1) get(k2) get(k1) put (k3) -> evict k2
# 3. ordered_map .. i'll rather not use this
# 4. multi guys trying to access at the same time? not for now

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, num_entries):
        # Implement this
        self.keyl = []
        self.mapl = {} # k -> (v, node)
        self.num_entries = num_entries
        self.head = None
    
    def _move(self, node):
        pass

    def printabout(f):
        def foo(self, *args):
            ret = f(self, *args)
            print(f"value after {f} is {self.__dict__}")
            return ret
        return foo
     
    @printabout
    def put(self, key, value):
        """
        If key already exists, replace the current value with the new value.
        If the key doesn't exist, add the new key/value entry to the cache.
        If the addition of the new entry causes the number of entries to exceed num_entries, remove the oldest entry based on the last time the entry is accessed (either through put or get).
        """
        if key in self.mapl:
            val, node = self.mapl[key]
            # a
            if node.next is not None:
                node.next.prev = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            self.head = node
            self.mapl[key] = (value, node)
            # a
        else:
            if len(self.mapl) < self.num_entries:
                # inti the node here
                nnode = Node(key)
                nnode.next = self.head
                if self.head is not None:
                    nnode.prev = self.head.prev
                    self.head.prev = nnode
                self.head = nnode
                self.mapl[key] = (value, nnode)
                # end of it
            else:
                evicted = self.head.prev # self.head cannot be none
                evicted.prev.next = self.head
                self.head.prev = evicted.prev
                del self.mapl[evicted.key]
                del evicted
                # whole thing
                nnode = Node(key)
                nnode.next = self.head
                if self.head is not None:
                    nnode.prev = self.head.prev
                    self.head.prev = nnode
                self.head = nnode
                self.mapl[key] = (value, nnode)

    @printabout
    def get(self, key):
            """Return the value associated with the key, or None if the key doesn't exist."""
            # Implement this
            if key not in self.mapl:
                return None
            val, node = self.mapl[key]
            # a
            if node.next is not None:
                node.next.prev = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev = node
            self.head = node
            return val

    
def test():
    c = LRUCache(2)
    
    # edge cases
    assert c.get(6) is None
    
    # inserts
    c.put(5, 25)
    assert c.get(5) == 25
    
    c.put(6, 36)
    c.get(5)
    c.put(7, 49)
    
    # basic ones
    assert c.get(6) is None
    assert c.get(5) == 25


test()

