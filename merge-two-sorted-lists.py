"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Runtime: 48 ms, faster than 24.86% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge Two Sorted Lists
        :param l1: ListNode Sorted Lists
        :param l2: ListNode Sorted Lists
        :return: ListNode Merged Sorted Lists
        """
        lv1: list = self.get_list(l1)
        lv2: list = self.get_list(l2)
        lv1.extend(lv2)
        lv1.sort()
        return self.get_list_node(lv1)

    def get_list(self, ln: ListNode) -> list:
        """
        Obtain List value from ListNode object.
        :param ln: ListNode ListNode object
        :return: list List value
        """
        l_ln: list = list()
        while ln:
            l_ln.append(ln.val)
            ln = ln.next
        return l_ln

    def get_list_node(self, lv: list) -> ListNode:
        """
        Obtain ListNode object from List value.
        :param lv: list List value
        :return: ListNode ListNode object
        """
        if len(lv) > 0:
            l_list_node: list = list()
            for e in lv:
                l_list_node.append(ListNode(e))
            l_list_node.reverse()
            for i in range(len(l_list_node)):
                if i > 0:
                    l_list_node[i].next = l_list_node[i - 1]
            return l_list_node[len(l_list_node) - 1]


s: Solution = Solution()
print('Example: ' + str(s.get_list(s.mergeTwoLists(s.get_list_node([1, 2, 4]), s.get_list_node([1, 3, 4])))))
print('Example Test 1: ' + str(s.get_list(s.mergeTwoLists(s.get_list_node([]), s.get_list_node([])))))
