"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
Runtime: 60 ms, faster than 61.57% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.5 MB, less than 5.97% of Python3 online submissions for Search Insert Position.
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        '''
        :param nums: list[int]
        :param target: int
        :return: int
        '''
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


s = Solution()
print('Example 1: ' + str(s.searchInsert([1, 3, 5, 6], 5)))
print('Example 2: ' + str(s.searchInsert([1, 3, 5, 6], 2)))
print('Example 3: ' + str(s.searchInsert([1, 3, 5, 6], 7)))
print('Example 4: ' + str(s.searchInsert([1, 3, 5, 6], 0)))
print('Example User 1: ' + str(s.searchInsert([-2, 1, 3, 5, 6], 0)))
