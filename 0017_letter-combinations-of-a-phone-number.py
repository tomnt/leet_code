"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Runtime: 32 ms, faster than 59.82% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.7 MB, less than 90.74% of Python3 online submissions for Letter Combinations of a Phone Number.
Amazon: On-Site Interview

Reference
https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8146/Clean-Python
"""


class Solution:
    def letterCombinations(self, digits: str) -> list:
        """
        :param str digits:
        :return List[str]:
        """
        l_digit = list(digits)
        l_char_button = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        comb = []
        for digit in l_digit:
            comb = [c1+c2 for c2 in l_char_button[digit] for c1 in comb or ['']]
            comb.sort()
        return comb


s = Solution()
print('Example 1: Expected: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], Actual: ',
      s.letterCombinations("23"))
