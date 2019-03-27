class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

    def __len__(self):
        length = 1
        nxt = self
        while nxt is not None:
            length += 1
            nxt = nxt.nxt
        return length

    def next(self):
        return self.nxt


def solver(l1, l2):
    s1 = len(l1)
    s2 = len(l2)

    if s1 > s2:
        # proceed d steps for l1
        for _ in range(s1 - s2):
            l1 = l1.next()
    else:
        # proceed d steps for l1
        for _ in range(s2 - s1):
            l2 = l2.next()

    while True:
        # move forward one level
        l1 = l1.next()
        l2 = l2.next()

        # exit condition
        if not l1:
            return

        # if same val, then return
        if l1 is l2:
            return l2


def test():
    # let's make a list 1 -> 3 --- 
    #                            |
    #                            -> 5 -> 9 -> 1
    #                            |
    #                        0 ---
    merge = Node(5, Node(9, Node(1, None)))

    # and the individual l's
    l1 = Node(1, Node(3, merge))
    l2 = Node(0, merge)

    # find the merger
    print(solver(l1, l2).val)
