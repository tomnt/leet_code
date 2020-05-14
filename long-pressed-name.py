"""
925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/
Runtime: 28 ms, faster than 80.65% of Python3 online submissions for Long Pressed Name.
Memory Usage: 14.1 MB, less than 14.29% of Python3 online submissions for Long Pressed Name.
https://leetcode.com/interview/2/
Success
Runtime: 36 ms
Memory Usage: 14.2 MB
"""


class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        :param str name: Name
        :param str typed: Key typed value
        :return bool:
        """
        dict_name = self.__get_dict_count_char(name)
        dict_typed = self.__get_dict_count_char(typed)
        for c_name in dict_name:
            if c_name in dict_typed:
                if dict_name[c_name] > dict_typed[c_name]:
                    return False
            else:
                return False
        for c_typed in dict_typed:
            if c_typed not in dict_name:
                return False
        return True

    @staticmethod
    def __get_dict_count_char(val: str) -> dict:
        dict_count_char = {}
        c_pointer = None
        c_key = None
        c_counter = 0
        count = 0
        for c in val:
            if c == c_pointer:
                c_counter += 1
            else:
                if c_counter > 0:
                    dict_count_char[c_key] = c_counter
                count += 1
                c_counter = 1
                c_pointer = c
                c_key = c + str(count)
        if c_counter > 0:
            dict_count_char[c_key] = c_counter
        return dict_count_char


s = Solution()
print("Example 1: Expected: True , Actual: ", s.isLongPressedName(name="alex", typed="aaleex"))
print("Example 2: Expected: False, Actual: ", s.isLongPressedName(name="saeed", typed="ssaaedd"))
print("Example 3: Expected: True , Actual: ", s.isLongPressedName(name="leelee", typed="lleeelee"))
print("Example 4: Expected: True , Actual: ", s.isLongPressedName(name="laiden", typed="laiden"))
print("Test 1   : Expected: False, Actual: ", s.isLongPressedName(name="xnhtq", typed="xhhttqq"))
print("Test 2   : Expected: False, Actual: ", s.isLongPressedName(name="alex", typed="alexxr"))
