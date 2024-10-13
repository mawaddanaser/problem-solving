class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        count = 0
        for word in words:
            if word[::-1] == word:
                return word
        return ""




