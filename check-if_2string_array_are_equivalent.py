class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        result1 = ""
        result2 = ""
        for word in range(0, len(word1)):
            result1 += word1[word]
        for word in range(0, len(word2)):
            result2 += word2[word]
        if result1 == result2:
            return True
        else:
            return False