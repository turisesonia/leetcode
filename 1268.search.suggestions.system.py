"""
# 1268
Medium
Search Suggestions System

https://leetcode.com/problems/search-suggestions-system

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.

Constraints:
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 104
- All the strings of products are unique.
- products[i] consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters.
"""

from typing import List


# Trie solution
class Solution:
    def __init__(self):
        self.links = {}

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in products:
            self._insert(product)

        return [self._search(searchWord[:i]) for i in range(1, len(searchWord) + 1)]

    def _insert(self, product: str):
        current = self.links

        prev = ""
        for char in product:
            word = prev + char
            if char not in current:
                current[char] = {"_word": word}

            prev = word
            current = current[char]

        current["_ended"] = True

    def _search(self, search: str):
        products = []

        current = self.links
        for char in search:
            if not current.get(char):
                current = None
                break

            current = current[char]

        if current is not None:
            stack = [current]
            while stack:
                node = stack.pop()

                for key, sub_node in node.items():
                    if key in ("_word", "_ended"):
                        continue

                    stack.append(sub_node)

                if node.get("_ended", False):
                    products.append(node["_word"])

        products.sort()

        return products[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = []

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]

            suggests = [product for product in products if product.startswith(prefix)]
            result.append(suggests[:3])

        return result


if __name__ == "__main__":
    suggestions = Solution().suggestedProducts(
        products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"
    )
    assert suggestions == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]

    suggestions = Solution().suggestedProducts(products=["havana"], searchWord="havana")
    assert suggestions == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
