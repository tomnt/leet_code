"""
872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
Runtime: 28 ms, faster than 88.23% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Leaf-Similar Trees.

https://leetcode.com/interview/2/
Success
Runtime: 44 ms
Memory Usage: 14 MB
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_leaf_values(root1, []) == self.get_leaf_values(root2, [])

    def get_leaf_values(self, r: TreeNode, v: list):
        if isinstance(r, TreeNode) and r.left == None and r.right == None:
            v.append(r.val)
        else:
            if isinstance(r.left, TreeNode):
                v = self.get_leaf_values(r.left, v)
            if isinstance(r.right, TreeNode):
                v = self.get_leaf_values(r.right, v)
        return v
