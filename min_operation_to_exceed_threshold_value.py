class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            if not nums[i] >= k:
                count += 1
        return count