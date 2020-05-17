"""
84. Largest Rectangle in Histogram (Hard)
https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/interview/3/
Time Limit Exceeded
"""


class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        """
        :param List[int] heights:
        :return int:
        """
        if len(heights) == 0:
            return 0
        list_area = []
        position = 0
        for height in heights:
            list_area.append(self.sum_back(position, heights) + height + self.sum_front(position, heights))
            position += 1
        return max(list_area)

    @staticmethod
    def sum_back(position: int, heights: list):
        total = 0
        for p in range(position - 1, -1, -1):
            if heights[p] >= heights[position]:
                total += heights[position]
            else:
                break
        return total

    @staticmethod
    def sum_front(position: int, heights: list):
        total = 0
        for p in range(position + 1, len(heights)):
            if heights[p] >= heights[position]:
                total += heights[position]
            else:
                break
        return total


s = Solution()
print("Example : Expected: 10, Actual:", s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print("Test    : Expected: 0, Actual:", s.largestRectangleArea([]))
