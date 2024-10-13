class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()

        result = 0
        for i in range(len(points) - 1):
            result = max(result, points[i + 1][0] - points[i][0])
        return result

    def maxWidthOfVerticalArea_2(self, points: list[list[int]]) -> int:
        return max([points[i + 1][0] - points[i][0] for i in range(len(points) - 1)])

solution = Solution()
solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]])
