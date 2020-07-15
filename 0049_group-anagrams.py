"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Amazon: Phone Interview
Runtime: 100 ms, faster than 83.34% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.6 MB, less than 88.12% of Python3 online submissions for Group Anagrams.
"""


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        """
        :param List[str] strs:
        :return List[List[str]]:
        """
        anagrams = {}
        for word in strs:
            anagram = "".join(sorted(word))
            if anagram in anagrams:
                anagrams[anagram].append(word)
            else:
                anagrams[anagram] = [word]
        return list(anagrams.values())


s = Solution()
print("Example 1: Expected:  [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']], Actual: ",
      s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print('Test 1: Expected:  [["",""]], Actual: ', s.groupAnagrams(["", ""]))

"""
        
        l_anagram = []
        s_added = set()
        checked = []
        for k1, s1 in enumerate(strs):
            if k1 not in s_added:
                s = list()
                s.append(s1)
                for k2 in range(k1 + 1, len(strs)):
                    s2 = strs[k2]
                    if self.get_sorted(s1) == self.get_sorted(s2):
                        s.append(s2)
                        s_added.add(k2)
                s.sort()
                l_anagram.append(s)
        return l_anagram

    d_sorted = {}
    def get_sorted(self, s: str) -> str:
        if s in self.d_sorted:
            return self.d_sorted[s]
        else:
            l_s = list(s)
            l_s.sort()
            s_sorted = ''.join(l_s)
            self.d_sorted[s] = s_sorted
            return s_sorted
"""
