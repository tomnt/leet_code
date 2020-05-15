"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
https://leetcode.com/interview/1/
Runtime: 1908 ms, faster than 5.05% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Implement Trie (Prefix Tree).

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__words = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.__words.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.__words

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return True in [word.startswith(prefix) for word in self.__words]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


trie = Trie()
trie.insert("apple")
print("Example : Expected True : , Actual:", trie.search("apple"))
print("Example : Expected False: , Actual:", trie.search("app"))
print("Example : Expected True : , Actual:", trie.startsWith("app"))
trie.insert("app")
print("Example : Expected True : , Actual:", trie.search("app"))
