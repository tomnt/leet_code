"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int)->int:
        abs_x=abs(x)
        list_abs_x = list(str(abs_x))
        list_abs_x.reverse()
        reverse_x = int(''.join(list_abs_x))
        if x < 0:
            reverse_x = int(reverse_x * -1)
        if -2**31 <= reverse_x < 2 ** 31:
            return reverse_x
        else:
            return 0


s = Solution()
# print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))
print(s.reverse(1534236469))
print(s.reverse(12345))
