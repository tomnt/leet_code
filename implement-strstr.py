"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
Runtime: 36 ms, faster than 80.50% of Python3 online submissions for Implement strStr().
Memory Usage: 14.1 MB, less than 12.31% of Python3 online submissions for Implement strStr().
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

s = Solution()
print('Example 1: '+str(s.strStr('hello','ll')))
print('Example 2: '+str(s.strStr('aaaaa','bba')))
