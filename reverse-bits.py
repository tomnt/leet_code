"""
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/

Runtime: 52 ms
Memory Usage: 13.9 MB
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b' + (str(bin(n))[2:]).zfill(32)[::-1], 0)


s = Solution()
print("Example : Expected: 964176192, Actual:", s.reverseBits(43261596))
print("Example : Expected: 3221225471, Actual:", s.reverseBits(4294967293))
