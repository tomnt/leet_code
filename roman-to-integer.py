"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/submissions/
"""


class Solution:
    def romanToInt(self, s: str)->int:
        d_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l_s = list(s)
        int_val = 0
        i_prev = 0
        for c in l_s:
            i = d_roman.get(c)
            if i_prev < i:
                i -= i_prev*2
            int_val += i
            i_prev = i
        return int_val


s = Solution()
l_input = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
for input in l_input:
    print(input + ' : ' + str(s.romanToInt(input)))
# s.romanToInteger('MCMXCIV')
ß