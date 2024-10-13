class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

    def getConcatenation_2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans_length = 2 * len(nums)
        ans = [0] * ans_length
        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
