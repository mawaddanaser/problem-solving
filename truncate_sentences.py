class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word_list = s.split()
        result = []
        for i in range(len(word_list)):
            if i < k:
                result.append(word_list[i])
                string = " ".join(result)
        return string

