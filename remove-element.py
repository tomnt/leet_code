class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        '''
        :param nums: list[int]
        :param val: int
        :return: int
        '''
        while val in nums:
            nums.remove(val)
        return len(nums)


s = Solution()
print('Example 1: ' + str(s.removeElement([3, 2, 2, 3], 3)))
print('Example 2: ' + str(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)))
print('Example User 1: ' + str(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 22)))


