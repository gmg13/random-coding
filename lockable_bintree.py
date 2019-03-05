import math
import random


class LBTree:
    def __init__(self, val, left=None, right=None):
        # define the base nodes
        self.val = val  # dummy for bug checking
        self.left = left
        self.right = right
        self.parent = None
        # augmented stuffs
        if left is not None:
            self.left.parent = self
        if right is not None:
            self.right.parent = self
        # locking related fields
        self.locked = False
        # ... all the decendents locked for this node
        self.descendents_locked = 0

    def __repr__(self):
        locked = "UNLOCKED"
        if self.locked:
            locked = "LOCKED"

        return f'[{self.val}-' \
            f'{locked}-{self.descendents_locked}, ' \
            f'{self.right}, {self.left}]'

    def canlock(self):
        # if any of the decendents locked, then no can do
        if self.descendents_locked > 0:
            return False
        # if any of the parents locked, then no can do too
        node = self.parent
        while True:
            if not node:
                return True
            if node.locked:
                return False
            node = node.parent

    def lock(self):
        # base case if locked myself
        if self.locked:
            return False
        if not self.canlock():
            return False
        # can lock, so lock it
        self.locked = True
        # and update all the ancestors
        node = self.parent
        while True:
            if not node:
                return True
            node.descendents_locked += 1
            node = node.parent

    def unlock(self):
        # base case if locked myself
        if not self.locked:
            return False
        if not self.canlock():
            return False
        # can lock, so lock it
        self.locked = False
        # and update all the ancestors
        node = self.parent
        while True:
            if not node:
                return True
            node.descendents_locked -= 1
            node = node.parent


def getp(height):
    "given the expected height of tree, calc the p"
    if height <= 0:
        return 0
    return math.exp(math.log(0.5) / height)


def gen_rand_tree(prefix, h):
    p = getp(h)
    left = right = None
    # gen left
    if random.random() < p:
        left = gen_rand_tree(f'{prefix}l', h - 1)
    # gen right
    if random.random() < p:
        right = gen_rand_tree(f'{prefix}r', h - 1)
    # gen this node too
    return LBTree(prefix, left, right)
