import re


class TrieNode:
    def __init__(self):
        self.word = ""
        self.cnt = 0
        self.links = [None] * 26


class Problem819:
    def __init__(self):
        self.res = ""
        self.max_ = 0

    def _insert(self, node: TrieNode, word: str):
        current = node

        for char in word:
            index = ord(char) - ord("a")

            if not current.links[index]:
                current.links[index] = self.TrieNode()
                current.links[index].word = current.word + char

            current = current.links[index]
        current.cnt += 1

    def _ban(self, node: TrieNode, word: str):
        current = node

        for char in word:
            index = ord(char) - ord("a")
            if not current.links[index]:
                return

            current = current.links[index]

        current.cnt = 0

    def _find_max(self, curr: TrieNode):
        if not curr:
            return

        if curr.cnt > self.max_:
            self.res = curr.word
            self.max_ = curr.cnt
        for i in range(len(curr.links)):
            self._find_max(curr.links[i])

    def most_common_word(self, paragraph: str, banned: list[str]) -> str:
        root = self.TrieNode()

        words = re.findall(r"\w+", paragraph.lower())

        for word in words:
            self._insert(root, word)

        for ban_word in set(banned):
            self._ban(root, ban_word)

        self._find_max(root)

        return self.res
