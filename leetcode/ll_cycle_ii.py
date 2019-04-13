# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        nodes = []
        head = self
        total = 3
        while total and head:
            nodes.append(head.val)
            head = head.next
            total -= 1
        return f'ListNode({nodes}...)'


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 'no cycle'
        # state tracker init
        slow = head
        fast = head
        i = 0
        # start the loop
        while True:
            if i % 2:
                slow = slow.next
            fast = fast.next
            i += 1

            # exit condition
            if not fast:
                return 'no cycle'
            if fast is slow:
                break
        # 0 1 2 3 4 5 6 3
        # 00, 01, 12, 13, 24, 25, 36, 33
        # 0 1 2 3 4 5 6 7 3
        # 00, 01, 12, 13, 24, 25, 36, 37, 43, 44
        # let's say the loop length is k and total length is l
        # slow has moved by x and fast has moved by y = 2*x + 1
        # number of times looped is n
        # if the loop length is k, loop is joined back at l - k
        # let's say meetup is z away from meetup
        # in first case, z = 0, k = 3, x = 3, y = 7, n = 0, l = 6
        # l + n*k + z + 1 = 1 + 2 * (l - k + z)
        # l + n*k + z + 1 = 1 + 2l -2k +2z
        # l - (n+2)*k + z = 0
        # l + z = (n + 2)*k
        # l + z - k = x = (n+1)
        # so x is a multiple of k .. therefore we can start from
        # start and the meeting point at the same time and meet
        # again at the same place in k time .. but rejoin first
        # happens at l - k

        start = head
        fast = fast.next
        j = 0
        while True:
            # exit condition again
            if start is fast:
                return f'tail connects to node index {j}'

            # and increments
            j += 1
            start = start.next
            fast = fast.next


def createll(nodes, loopback):
    sentinel = ListNode(0)
    head = sentinel
    for n in nodes:
        head.next = ListNode(n)
        head = head.next
    if loopback == -1:
        return sentinel.next
    # so loopback is present
    tail = head
    connection = sentinel.next
    while loopback:
        connection = connection.next
        loopback -= 1
    # and connect the tail to the node
    tail.next = connection
    # and return the node
    return sentinel.next
