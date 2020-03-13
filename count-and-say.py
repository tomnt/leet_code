class Solution:
    def countAndSay(self, n: int) -> str:
        """
        :param n: int Example: 4
        :return: str: '1211'
        """
        if n <= 1:
            return '1'
        val = '1'
        for i in range(n-1):
            val = self.__read_off(val)
        return val

    def __read_off(self, val: str)->str:
        """
        :param val: str Example: '21'
        :return:  str Example: '1211'
        """
        l_l_count = self.__count(val)
        read_off = str()
        for l_count in l_l_count:
            read_off += str(l_count[0])
            read_off += l_count[1]
        return read_off

    def __count(self, val: str) -> list:
        """
        :param val: str Example: '21'
        :return: list Example: [[1, '2'], [1, '1']]
        """
        l_l_count = []
        count = 1
        c_tmp = ''
        for c in list(val):
            if c_tmp == c:
                count += 1
            else:
                l_count = self.__get_l_count(count, c_tmp)
                if c_tmp:
                    l_l_count.append(l_count)
                count = 1
            c_tmp = c
        l_count = self.__get_l_count(count, c_tmp)
        l_l_count.append(l_count)
        return l_l_count

    @staticmethod
    def __get_l_count(count: int, c: str) -> list:
        """
        :param count: int Example: 2
        :param c: srt Example: '1'
        :return: list Example: [2, '1']
        """
        l_count = list()
        l_count.append(count)
        l_count.append(c)
        return l_count


'''
https://leetcode.com/problems/count-and-say/
Details 
Runtime: 40 ms, faster than 75.17% of Python3 online submissions for Count and Say.
Memory Usage: 13.9 MB, less than 6.38% of Python3 online submissions for Count and Say.
Next challenges:
'''
s = Solution()

print('Example 0: '+s.countAndSay(0))
print('Example 1: '+s.countAndSay(1))
print('Example 2: '+s.countAndSay(2))
print('Example 3: '+s.countAndSay(3))
print('Example 4: '+s.countAndSay(4))
print('Example 5: '+s.countAndSay(5))
print('Example 8: '+s.countAndSay(8))
print('Example 10: '+s.countAndSay(10))
