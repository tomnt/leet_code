"""
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Runtime: 1816 ms, faster than 9.65% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 17.8 MB, less than 8.70% of Python3 online submissions for Kth Largest Element in a Stream.

Random question set from a real company. Question 2
"""


class KthLargest:

    def __init__(self, k: int, nums: list):
        """
        :param int k:
        :param List[int] nums:
        """
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


k = 3
arr = [4, 5, 8, 2]
kthLargest = KthLargest(3, arr)

print("Expected: 4, Actual:", kthLargest.add(3))
print("Expected: 5, Actual:", kthLargest.add(5))
print("Expected: 5, Actual:", kthLargest.add(10))
print("Expected: 8, Actual:", kthLargest.add(9))
print("Expected: 8, Actual:", kthLargest.add(4))
