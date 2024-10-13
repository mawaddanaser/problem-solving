def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        result = 0
        for i in range(0, len(nums)):
            ones_count = bin(i).count("1")
            if ones_count == k:
                result += nums[i]
        return result


def sumIndicesWithKSetBits_2(self, nums: list[int], k: int) -> int:
    return sum([nums[i] for i in range(len(nums)) if bin(i).count("1") == k])