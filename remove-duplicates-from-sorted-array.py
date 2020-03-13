class Solution:
    def removeDuplicates(self, nums: list) -> int:
        """
        Remove the duplicates in-place such that each element appear only once and return the new length.
        :param nums: List[int] List to remove duplication. Example: [1,1,2]
        :return: int Length after removing duplication. Example: 2
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                del (nums[i+1])
        # print(nums)  # TODO: Remove. For Test.
        return len(nums)


s = Solution()
print('Example 1: ' + str(s.removeDuplicates([1, 1, 2])))
print('Example 2: ' + str(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])))

print('User Test 1: ' + str(s.removeDuplicates([])))
print('User Test 2: ' + str(s.removeDuplicates([-1000, -50, 0, 1, 1, 1, 1, 1, 20, 300, 4000, 50000])))
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
26. Remove Duplicates from Sorted Array
Runtime: 96 ms, faster than 78.07% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.7 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
Next challenges:
'''

'''
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        """
        Remove the duplicates in-place such that each element appear only once and return the new length.
        :param nums: List[int] List to remove duplication. Example: [1,1,2]
        :return: int Length after removing duplication. Example: 2
        """
        loop: bool = True
        while loop:
            l_num: list = []
            loop: bool = False
            for i in range(len(nums)):
                if nums[i] in l_num:
                    del (nums[i])
                    loop = True
                    break
                else:
                    l_num.append(nums[i])
        nums.sort()
        print(nums)  # TODO: Remove. This is for test
        return len(nums)
'''
