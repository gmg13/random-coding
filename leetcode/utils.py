from collections import deque
from typing import Optional


class DLLNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_level_order(li: list) -> Optional[TreeNode]:
    "create a tree node from level order list of nodes"
    if not li:
        return None

    # index of items
    index = 0
    # bag of level order node items
    bag = deque()
    # initialize this to the root TreeNode
    root = TreeNode(li[index], None, None)
    bag.append(root)
    # raise index
    index += 1

    while(bag and index < len(li)):
        # get the essentials
        item = bag.popleft()
        left = li[index]
        right = li[index + 1]
        index += 2
        # update left item
        if left is not None:
            item.left = TreeNode(left, None, None)
            bag.append(item.left)
        # update right item
        if right is not None:
            item.right = TreeNode(right, None, None)
            bag.append(item.right)

    return root
