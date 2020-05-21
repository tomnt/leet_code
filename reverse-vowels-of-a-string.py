"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
Time Limit Exceeded

Runtime: 8760 ms
Memory Usage: 20.2 MB
https://leetcode.com/interview/1/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        list_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', ]
        list_s = list(s)
        r_dict_s = Solution.get_r_dict_s(list_s, list_vowel)
        list_char_reversed_vowels = []
        position = 0
        for c in list_s:
            if c in list_vowel:
                list_char_reversed_vowels.append(list_s[r_dict_s[position]])
            else:
                list_char_reversed_vowels.append(c)
            position += 1
        return "".join(list_char_reversed_vowels)

    @staticmethod
    def get_r_dict_s(list_s: list, list_vowel: list):
        # set list_desc_key, dict_position
        dict_position = {}
        position = 0
        for c in list_s:
            if c in list_vowel:
                dict_position[position] = c
            position += 1
        list_desc_key = [sorted(dict_position, reverse=True)][0]
        # get r_dict_s
        position = 0
        r_dict_s = {}
        for key_desc in list_desc_key:
            key_r = list(dict_position)[position]
            r_dict_s[key_r] = key_desc
            position += 1
        return r_dict_s


s = Solution()
print('Example 1: Expected: "holle", Actual:', s.reverseVowels("hello"))
print('Example 2: Expected: "leotcede", Actual:', s.reverseVowels("leetcode"))
print('Test 1   : Expected: "Aa", Actual :', s.reverseVowels("aA"))
