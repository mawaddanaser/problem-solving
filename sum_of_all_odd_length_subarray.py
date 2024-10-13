class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        output = 0
        for i in range(1, len(arr) + 1, 2):
            output += sum([sum(arr[j:j+i]) for j in range(len(arr) - i + 1)])
        return output

    def sumOddLengthSubarrays_2(self, arr: list[int]) -> int:
        return sum([sum(arr[j:j + i]) for i in range(1, len(arr) + 1, 2) for j in range(len(arr) - i + 1)])

        