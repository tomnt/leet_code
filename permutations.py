"""
46. Permutations
https://leetcode.com/problems/permutations/
https://leetcode.com/interview/1/
Runtime: 32 ms, faster than 96.70% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import itertools


class Solution:
    def permute(self, nums: list) -> list:
        """
        :param nums: List[int] nums:
        :return List[List[int]]:
        """
        return list(itertools.permutations(nums))


s = Solution()
print("Example : Expected: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)],"
      + '\n' + "            Actual:", s.permute([1, 2, 3]))
