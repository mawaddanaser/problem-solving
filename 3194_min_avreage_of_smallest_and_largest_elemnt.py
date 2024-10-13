nums = [7, 8, 3, 4, 15, 13, 4, 1]
n =len(nums)
for i in range( n // 2):
    minElement = min(nums)
    nums.remove(minElement)
