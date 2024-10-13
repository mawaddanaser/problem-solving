class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i in range(len(words)) if x in words[i]]

    def findWordsContaining_2(self, words: list[str], x: str) -> list[int]:
        result = []
        for word in words:
            if x in word:
                result.append(words.index(word))

        return result
