class Solution:
    def isPalindrome(self, x: int)->bool:
        reversed_x=str(x)[::-1]
        if str(x) == reversed_x:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
