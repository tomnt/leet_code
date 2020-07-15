"""
1160. Find Words That Can Be Formed by Characters
Amazon: Online Assessment
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

Runtime: 1992 ms, faster than 5.08% of Python3 online submissions for Find Words That Can Be Formed by Characters.
Memory Usage: 14.2 MB, less than 69.39% of Python3 online submissions for Find Words That Can Be Formed by Characters.
"""

class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        """
        :param List[str] words:
        :param str chars:
        :return:
        """
        words_org = words.copy()
        set_index_words = set()
        for i_chars, ch in enumerate(chars):
            for index_words, word in enumerate(words):
                index_char = self.get_index(ch, word)
                if index_char != -1:
                    new_word = word[:index_char] + word[index_char + 1:]
                    words[index_words] = new_word
                    set_index_words.add(index_words)
        count_characters = 0
        for index_words,word in enumerate(words):
            if len(word) == 0:
                count_characters += len(words_org[index_words])
        return count_characters

    def get_index(self, c: chr, word: str):
        for index, char in enumerate(word):
            if char == c:
                return index
        return -1


s = Solution()
print("Example 1: Expected: 6, Actual: ", s.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
print("Example 2: Expected: 10, Actual: ", s.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
