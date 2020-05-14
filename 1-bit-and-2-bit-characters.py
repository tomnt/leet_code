"""
717. 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/

Runtime: 56 ms, faster than 30.91% of Python3 online submissions for 1-bit and 2-bit Characters.
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for 1-bit and 2-bit Characters.

Random question set from a real company. Question 1
Runtime: 52 ms
Memory Usage: 14.1 MB
"""


class Solution:
    def isOneBitCharacter(self, bits: list) -> bool:
        """
        :param List[int] bits:
        :return bool:
        """
        dict_bits = dict(enumerate(bits))
        skip = False
        is_one_bit = False
        for k in dict_bits:
            if skip:
                skip = False
            else:
                if dict_bits[k] == 1:
                    skip = True
                    is_one_bit = False
                else:
                    is_one_bit = True
        return is_one_bit


s = Solution()
print("Example 1: Expected: True , Actual: ", s.isOneBitCharacter([1, 0, 0]))
print("Example 2: Expected: False, Actual: ", s.isOneBitCharacter([1, 1, 1, 0]))
