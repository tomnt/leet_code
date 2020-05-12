"""
292. Nim Game
https://leetcode.com/problems/nim-game/

Runtime: 28 ms, faster than 71.08% of Python3 online submissions for Nim Game.
Memory Usage: 13.9 MB, less than 14.29% of Python3 online submissions for Nim Game.
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        count = 0
        while n > 0:
            if n % 4 == 0:
                return False
            elif n <= 7:
                return True
            elif n > 7:
                if n % 4 == 1:
                    return True
                n -= 1
                count += 1


s = Solution()
print('n=1: True : ', s.canWinNim(1))
print('n=2: True : ', s.canWinNim(2))
print('n=4: False: ', s.canWinNim(4))
print('n=7: True : ', s.canWinNim(7))
print('n=8: False: ', s.canWinNim(8))
print('n=9: True : ', s.canWinNim(9))
