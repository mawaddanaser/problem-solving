class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    def runningSum_2(self, nums: list[int]) -> list[int]:
        a = 0
        result = []
        for i in nums:
            a = i + a

            result.append(a)
        return result

solution = Solution()
solution.runningSum([1,2,3,4])


