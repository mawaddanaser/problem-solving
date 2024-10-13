class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [None] * (len(nums))
        for i in range(0, len(nums)):
            ans[i] = nums[nums[i]]

        return ans
    
    def buildArray_2(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(0, len(nums))]

