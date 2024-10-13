def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1

    return -1


numbers = [1, 3, 4, 5, 6, 7, 8, 9, 10]
num = -2
print(binary_search(numbers, num))


def recursive_binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
            return recursive_binary_search(nums[left:], target)
        if nums[mid] > target:
            right = mid - 1
            return recursive_binary_search(nums[:right], target)
