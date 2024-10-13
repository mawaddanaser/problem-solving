class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        subarrays = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j + 1]
                subarrays.append(subarray)

        distinct_counts = []
        for subarray in subarrays:
            distinct_count = len(set(subarray))
            distinct_counts.append(distinct_count)

        return sum([count ** 2 for count in distinct_counts])

