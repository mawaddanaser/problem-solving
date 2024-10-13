class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in arr1:
            if all([abs(i - j) > d for j in arr2]):
                count += 1
        return count

    def findTheDistanceValue_2(self, arr1: list[int], arr2: list[int], d: int) -> int:
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)