class Solution:
    def convertToBase7(self, num: int)->str:
        if abs(num) < 7:
            return str(num)
        base7: str = ''
        is_negative: bool = num < 0
        num = abs(num)
        while num > 0:
            remainder = num % 7
            base7 = str(remainder) + base7
            num = num//7
        if is_negative:
            base7 = '-'+base7
        return base7

s = Solution()
#print(s.convertToBase7(100))
#print(s.convertToBase7(-7))
#print(s.convertToBase7(-100))
#print(s.convertToBase7(0))
#print(s.convertToBase7(-5))
#print(s.convertToBase7(5))
