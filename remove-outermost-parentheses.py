"""
1021. Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/
Runtime: 52 ms, faster than 12.80% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 15.4 MB, less than 5.56% of Python3 online submissions for Remove Outermost Parentheses.
"""
import itertools


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        list_s = list(S)
        dict_s = dict(enumerate(list_s))
        list_num_p = [{'(': 1, ')': -1}[p] for p in list_s]
        dict_acc = dict(enumerate(itertools.accumulate(list_num_p)))
        is_open = False
        for k in dict_acc:
            if not is_open and dict_acc[k] == 1:
                is_open = True
                dict_s.pop(k)
            if dict_acc[k] == 0:
                is_open = False
                dict_s.pop(k)
        return ''.join([dict_s[k] for k in dict_s])


s = Solution()
print("Example : Expected: ()()(), Actual:", s.removeOuterParentheses("(()())(())"))
print("Example : Expected: ()()()()(()), Actual:", s.removeOuterParentheses("(()())(())(()(()))"))
