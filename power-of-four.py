"""
342. Power of Four
https://leetcode.com/problems/power-of-four/
Runtime: 48 ms, faster than 6.44% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for Power of Four.

Runtime: 28 ms
Memory Usage: 14 MB
"""
import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return math.log(num, 1 / 4) % 1 == 0 if num > 0 else False


s = Solution()
print("Example 1: Expected: True , Actual:", s.isPowerOfFour(16))
print("Example 2: Expected: False, Actual:", s.isPowerOfFour(5))
print("My test 1: Expected: False, Actual:", s.isPowerOfFour(-2147483648))
print("My test 2: Expected: False, Actual:", s.isPowerOfFour(36))
print("My test 3: Expected: False, Actual:", s.isPowerOfFour(0))
print("My test 4: Expected: False, Actual:", s.isPowerOfFour(-4))
