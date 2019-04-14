# code
# howdy!! yeowhhww


# somehow this is not required this time around
def main():
    # get the number of cases
    ncases = int(input())
    # and loop through
    for _ in range(ncases):
        n = int(input())
        arr = [int(i) for i in input().split()][:n]
        # and run the algorithm
        print(arr[int(n / 2)])

# instead they need a function problem .. well.. be consistent!
# and next time .. follow pip8


def findMid(head):
    slow = head
    fast = head
    i = 0

    while fast:
        if i % 2:
            slow = slow.next
        fast = fast.next
        i += 1
    # return it
    return slow


class node:
    # Node Class
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)
