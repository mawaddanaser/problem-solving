class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if (nums[j] - nums[i] == diff and nums[j] > nums[i] and
                        nums[k] - nums[j] == diff and nums[k] > nums[j]):
                        count += 1
        return count
