class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(0 , len(sorted_nums)):
            if sorted_nums [i] == target:
                res.append(i)
        return res