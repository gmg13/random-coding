from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

MIN = -2**63
class Solution:
    def _one_sided_path(self, node: Optional[TreeNode]):
        """returns max leaf-path which is a path from
        node to leaf and the max "path" as described in
        problem so far"""
        if not node:
            return (0, 0)
        lt_lp, lt_maxp, rt_lp, rt_maxp = 0, MIN, 0, MIN
        if node.right:
            rt_lp, rt_maxp = self._one_sided_path(node.right)
        if node.left:
            lt_lp, lt_maxp = self._one_sided_path(node.left)

        # now let's cover all the cases
        # print(node.val, lt_lp, lt_maxp, rt_lp, rt_maxp)
        return (
            max(node.val, node.val + lt_lp, node.val + rt_lp),
            max(
                lt_maxp,
                rt_maxp,
                node.val,
                node.val + lt_lp,
                node.val + rt_lp,
                node.val + lt_lp + rt_lp
            ))


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self._one_sided_path(root)[1]
