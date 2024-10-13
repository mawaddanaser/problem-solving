class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split(" ")
        temp = []
        for word in sentence:
            temp.append((int(word[-1]), word.removesuffix(word[-1])))

        s_temp = sorted(temp)
        return " ".join([i[1] for i in s_temp])

