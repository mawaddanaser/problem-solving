class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        output = 0
        dic_s = {letter: index for index, letter in enumerate(s)}
        dic_t = {letter: index for index, letter in enumerate(t)}

        for letter_s, index_s in dic_s.items():
            for letter_t, index_t in dic_t.items():
                if letter_s == letter_t:
                    output += abs(index_s - index_t)
        return output            