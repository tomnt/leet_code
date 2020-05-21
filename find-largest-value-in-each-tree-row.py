"""
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
Runtime: 60 ms, faster than 17.05% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.7 MB, less than 20.00% of Python3 online submissions for Find Largest Value in Each Tree Row.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not isinstance(root, TreeNode):
            return []
        self.dict_level = {0: []}
        self.set_dict_level(root)
        largest_values = []
        for k in self.dict_level:
            largest_values.append(max(self.dict_level[k]))
        return largest_values

    def set_dict_level(self, node: TreeNode, level=0):
        if level not in self.dict_level:
            self.dict_level[level] = []
        self.dict_level[level].append(node.val)
        if node.left is not None:
            self.set_dict_level(node.left, level + 1)
        if node.right is not None:
            self.set_dict_level(node.right, level + 1)
