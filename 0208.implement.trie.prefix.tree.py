"""
# 208
Medium
Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
* `Trie()` Initializes the trie object.
* `def insert(String word)` Inserts the string word into the trie.
* `def search(String word) -> bool` Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
* `def startsWith(String prefix) -> bool` Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""


class Trie:
    def __init__(self):
        self.links = {}

    def insert(self, word: str) -> None:
        """
        Insert word, save every alphabet to links

        Example:
        "apple" => a -> ap -> app -> appl -> apple (is word)

        in dictionary
        "apple" => {a: {p: {p: {l: {e:{is_word:True}}}}}}
        """
        curr = self.links

        for char in word:
            if char not in curr:
                curr[char] = {}

            curr = curr[char]

        curr["is_word"] = True

    def search(self, word: str) -> bool:
        """
        Search this word is exists in links

        Full match
        """
        curr = self.links

        for char in word:
            if not curr.get(char):
                return False

            curr = curr[char]

        return curr.get("is_word", False)

    def startsWith(self, prefix: str) -> bool:
        """
        Find prefix is exists in links

        Like match
        """
        curr = self.links

        for char in prefix:
            if not curr.get(char):
                return False

            curr = curr[char]

        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")

    trie.insert("app")

    assert trie.search("app")
