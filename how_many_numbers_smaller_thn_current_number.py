class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        # nums.sort()
        for i in range(0, len(nums)):
            a = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j] and j != i:
                    a += 1
            result.append(a)

        return result


solution = Solution()
solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
