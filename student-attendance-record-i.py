"""
551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/
Runtime: 24 ms
Memory Usage: 13.9 MB
Runtime: 24 ms, faster than 88.94% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 13.5 MB, less than 11.11% of Python3 online submissions for Student Attendance Record I.
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        list_s: str = list(s)
        count_a = 0
        count_l = 0
        for code in list_s:
            if code == 'A':
                count_a += 1
                if count_a > 1:
                    return False
            if code == 'L':
                count_l += 1
                if count_l > 2:
                    return False
            else:
                count_l = 0
        return True


s = Solution()
print('Example 1: True : ', s.checkRecord("PPALLP"))
print('Example 2: False: ', s.checkRecord("PPALLL"))
