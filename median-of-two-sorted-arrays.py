class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        nums1.extend(nums2)
        nums1.sort()
        nums1_len: int = len(nums1)
        if nums1_len % 2:  # When extended array length is odd number
            return nums1[nums1_len // 2]
        else:  # When extended array length is even number
            return (nums1[(nums1_len // 2) - 1] + nums1[nums1_len // 2]) / 2


s = Solution()
print("Example 1: " + str(s.findMedianSortedArrays([1, 3], [2])))
print("Example 2: " + str(s.findMedianSortedArrays([1, 2], [3, 4])))
print("User Test 1: " + str(s.findMedianSortedArrays([], [1])))
print("User Test 2: " + str(s.findMedianSortedArrays([1], [])))


'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
4. Median of Two Sorted Arrays

Runtime: 112 ms, faster than 49.68% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

Test case
[1,3]
[2]
'''