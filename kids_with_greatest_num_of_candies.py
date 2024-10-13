class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candies = max(candies)

        for candy in candies:
            total_candies = candy + extraCandies
            if total_candies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result