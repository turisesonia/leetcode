"""
# 345
Easy

https://leetcode.com/problems/reverse-vowels-of-a-string

Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
vowels = [e, o], reverse = [o, e]
Output: "holle"

Example 2:
Input: s = "leetcode"
vowels = [e, e, o, e], reverse = [e, o, e, e]
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.


"""


def reverse_vowels(s: str) -> str:
    vowels = "aeiou"

    l = 0
    r = len(s) - 1
    s = list(s)

    while l < r:
        char_l = s[l].lower()
        char_r = s[r].lower()

        if char_l not in vowels:
            l += 1
            continue

        if char_r not in vowels:
            r -= 1
            continue

        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return "".join(s)


if __name__ == "__main__":
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels(" ") == " "
