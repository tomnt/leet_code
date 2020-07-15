"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Amazon: Phone Interview
Runtime: 56 ms, faster than 8.76% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 45.47% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        closure = {')': '(', '}': '{', ']': '['}
        opener = ['(', '{', '[']
        opened = []
        for c in list(s):
            if c in opener:
                opened.append(c)
            if c in closure:
                if closure[c] in opener and closure[c] in opened and len(opened) > 0:
                    if opened[-1] == closure[c]:
                        opened.pop(-1)
                else:
                    return False
        return len(opened) == 0


s = Solution()
print("Example 1: Expected: true , Actual: ", s.isValid("()"))
print("Example 2: Expected: true , Actual: ", s.isValid("()[]{}"))
print("Example 3: Expected: false, Actual: ", s.isValid("(]"))
print("Example 4: Expected: false, Actual: ", s.isValid("([)]"))
print("Example 5: Expected: true , Actual: ", s.isValid("{[]}"))
print("Test 1: Expected: true , Actual: ", s.isValid("]"))
print("Test 2: Expected: false , Actual: ", s.isValid("(])"))
