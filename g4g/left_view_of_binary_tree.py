from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i


def printLeftView(root):
    # don't print nothing .. return
    if not root:
        print()
        return
    # initialize queue and left view components
    lv = []
    q = deque()
    q.append((root, 0))

    # now BFS
    while q:
        node, lvl = q.popleft()
        # insert if in left view
        if lvl >= len(lv):
            lv.append(node.data)
        if node.left:
            q.append((node.left, lvl + 1))
        if node.right:
            q.append((node.right, lvl + 1))

    # and print the left view
    print(*lv, end='')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print('')
            continue
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k += 3
        printLeftView(root)
        print('')
