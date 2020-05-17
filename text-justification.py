"""
68. Text Justification (Hard)
https://leetcode.com/problems/text-justification/

Runtime: 24 ms, faster than 92.31% of Python3 online submissions for Text Justification.
Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Text Justification.
"""


class Solution:
    def fullJustify(self, words: list, maxWidth: int) -> list:
        """
        :param List[str] words: Words
        :param int maxWidth: Max width
        :return List[str]: List of strings
        """
        list_phrase = []
        accumulation = 0
        position_prev = 0
        position = 0
        for word in words:
            accumulation += len(word) + 1
            if accumulation - 1 > maxWidth:
                list_phrase.append(self.implode(words[position_prev:position], maxWidth, False))
                accumulation = len(word) + 1
                position_prev = position
            if position == len(words) - 1:
                list_phrase.append(self.implode(words[position_prev:len(words)], maxWidth, True))
            position += 1
        return list_phrase

    @staticmethod
    def implode(words: list, maxWidth: int, is_last: bool):
        space_length = maxWidth - sum([len(word) for word in words]) - (len(words) - 1)
        if len(words) == 1:
            return words[0] + " " * space_length
        if is_last:
            return " ".join(words) + " " * space_length
        quotient = space_length // (len(words) - 1)
        remainder = space_length % (len(words) - 1)
        for i in range(0, remainder):
            words[i] = words[i] + " "
        for i in range(0, len(words) - 1):
            words[i] = words[i] + " " * quotient
        return " ".join(words)


s = Solution()
print("Example 1: ",
      s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print("Example 2: ", s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print("Example 3: ", s.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                                    "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
print("Test 1   : ", s.fullJustify(
    ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
     "your", "country"], 20))
