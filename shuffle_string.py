class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_s = [None] * len(s)
        for ch, i in list(zip(s, indices)):
            shuffled_s[i] = ch
        return "".join(shuffled_s)
