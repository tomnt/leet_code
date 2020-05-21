"""
832. Flipping an Image
https://leetcode.com/problems/flipping-an-image/
Runtime: 56 ms, faster than 31.50% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.8 MB, less than 6.00% of Python3 online submissions for Flipping an Image.

https://leetcode.com/interview/1/
Success
Runtime: 56 ms
Memory Usage: 13.9 MB
"""


class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        """
        :param List[List[int]] A:
        :return  List[List[int]:
        """
        dict_invert = {0: 1, 1: 0}
        k1 = 0
        for l in A:
            l.reverse()
            for k2 in range(0, len(l)):
                l[k2] = dict_invert[l[k2]]
            A[k1] = l
            k1 += 1
        return A


s = Solution()
print('Example 1: Expected: [[1,0,0],[0,1,0],[1,1,1]], Actual:', s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print('Example 2: Expected: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]], Actual:',
      s.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
print('My test 1: Expected: [], Actual:', s.flipAndInvertImage([]))