class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_list = []
        element_sum = sum(nums)

        for num in nums:
            digit_list.extend([int(digit) for digit in str(num)])

        digit_sum = sum(digit_list)
        absolute_diff = abs(element_sum - digit_sum)
        return absolute_diff
