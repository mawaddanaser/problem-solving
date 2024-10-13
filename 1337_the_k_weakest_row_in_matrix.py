class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []

        for i, row in enumerate(mat):
            count = sum(row)
            temp.append((count, i))

        temp.sort()
        return [j[1] for j in temp][:k]



