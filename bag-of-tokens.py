"""
948. Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/
"""


class Solution:
    def bagOfTokensScore(self, tokens: list[int], P: int)-> int:
        score = 0
        for token in tokens:
            if P >= token:
                score += 1
        return score


s = Solution()
print(s.bagOfTokensScore([100, 200], 150))


