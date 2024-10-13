class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        for i in range(0, len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                return (sorted_nums[i] - 1) * (sorted_nums[j] - 1)

