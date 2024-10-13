# class Solution:
#     def leftRightDifference(self, nums: list[int]) -> list[int]:
#         left_arr = []
#         right_arr = []
#
# solution = Solution()
# solution.leftRightDifference([10,4,8,3])

nums = [10,4,8,3]
left_arr = []
right_arr = []
def leftRightDifference():
    for i in range(1, len(nums)):
        left_arr[i] += nums[i - 1]
    return left_arr



leftRightDifference()