"""
1176. Diet Plan Performance
https://leetcode.com/problems/diet-plan-performance/
Amazon: Online Assessment
Runtime: 248 ms
Memory Usage: 23 MB
You are free to continue working on this question, but please note that only your first accepted submission will be counted.
"""


class Solution:
    def dietPlanPerformance(self, calories: list, k: int, lower: int, upper: int) -> int:
        """
        :param List[int] calories:
        :param int k:
        :param int lower:
        :param int upper:
        :return:
        """
        performance = 0
        for i in range(0, len(calories) + 1 - k):
            if k == 1:
                cal_window = calories[i]
            else:
                if i == 0:
                    cal_window = sum([calories[i2] for i2 in range(i, i + k)])
                else:
                    cal_window = cal_window - calories[i-1] + calories[i+k-1]
            if cal_window < lower:
                performance -= 1
            if cal_window > upper:
                performance += 1
        return performance


s = Solution()
print("Example 1: Expected: 0, Actual: ", s.dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))
print("Example 2: Expected: 1, Actual: ", s.dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1))
print("Example 3: Expected: 0, Actual: ", s.dietPlanPerformance(calories=[6, 5, 0, 0], k=2, lower=1, upper=5))
