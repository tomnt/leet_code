"""
671. Second Minimum Node In a Binary Tree
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Runtime: 24 ms, faster than 91.57% of Python3 online submissions for Second Minimum Node In a Binary Tree.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Second Minimum Node In a Binary Tree.

https://leetcode.com/interview/1/submissions/
Success
Details
Runtime: 28 ms
Memory Usage: 13.9 MB
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.list_node = []
        self.set_list(root)
        result = sorted(set(self.list_node))
        if len(result) > 1:
            return result[1]
        else:
            return -1

    def set_list(self, root: TreeNode) -> list:
        self.list_node.append(root.val)
        if root.left != None:
            self.set_list(root.left)
        if root.right != None:
            self.set_list(root.right)

#s = Solution()
#print("Example 1: Expected 5 : , Actual:", s.findSecondMinimumValue([4, 1, 8, 7]))

