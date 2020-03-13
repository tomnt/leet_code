# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i1: int = self.get_int(l1)
        i2: int = self.get_int(l2)
        return self.get_list_node(i1 + i2)

    def get_int(self, ln: ListNode) -> int:
        l_c: list = list()
        while True:
            l_c.append(str(ln.val))
            if not ln.next:
                break
            ln = ln.next
        l_c.reverse()
        return int(''.join(l_c))

    def get_list_node(self, i: int) -> ListNode:
        l_s_i: list = list(str(i))
        ln: ListNode = ListNode(l_s_i[0])
        for i in range(1, len(l_s_i)):
            ln_next = ln
            ln = ListNode(l_s_i[i])
            ln.next = ln_next
        return ln


s = Solution()
print("Example: "+str(s.get_int(s.addTwoNumbers(s.get_list_node(342),s.get_list_node(465)))))

'''
https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
Test case
    [2,4,3]
    [5,6,4]
Success
Details 
    Runtime: 76 ms, faster than 79.10% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
'''