"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        l_s = list(s)
        d_open = {'(': 0, '{': 1, '[': 2}
        d_close = {')': 0, '}': 1, ']': 2}
        l_tmp = []
        for c in l_s:
            if c in d_open:
                l_tmp.append(d_open.get(c))
            if c in d_close:
                if len(l_tmp) > 0 and l_tmp[-1] == d_close.get(c):
                    l_tmp.pop()
                else:
                    return False
        if len(l_tmp) == 0:
            return True
        else:
            return False


s = Solution()
print('Example 1: '+str(s.isValid("()")))
print('Example 2: '+str(s.isValid("()[]{}")))
print('Example 3: '+str(s.isValid("(]")))
print('Example 4: '+str(s.isValid("([)]")))
print('Example 5: '+str(s.isValid("{[]}")))
print('Submit 1: '+str(s.isValid("]")))
print('Submit 2: '+str(s.isValid("[")))
