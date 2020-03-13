class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        i = 0
        for index, num in enumerate(nums):
            other = target - num
            print(i)
            i += 1
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
