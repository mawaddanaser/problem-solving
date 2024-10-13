class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in c:
                return i

    def missingNumber_2(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i