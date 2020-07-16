"""
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Amazon: Onsite Interview
Runtime: 812 ms, faster than 5.25% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 16 MB, less than 64.68% of Python3 online submissions for Two Sum IV - Input is a BST.

Reference: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/424525/Python-3-or-Recursive-or-Beats-99.96
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def search(node: TreeNode, save: list):
            if not node:
                return False
            diff = k - node.val
            if diff in save:
                return True
            save.append(node.val)
            return search(node.right, save) or search(node.left, save)
        return search(root, [])


s = Solution()
print("Example 1: Expected: True , Actual: ",
      s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), (TreeNode(4))), TreeNode(6, None, TreeNode(7))), 9))
print("Example 2: Expected: False, Actual: ",
      s.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), (TreeNode(4))), TreeNode(6, None, TreeNode(7))), 28))
