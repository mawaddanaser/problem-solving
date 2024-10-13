class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(0, len(nums)):
            new_item = min(nums)
            nums.remove(new_item)
            arr.append(new_item)

        for i in range(0, len(arr), 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr



def numberGame_2(self, nums: list[int]) -> list[int]:
    nums.sort()
    arr = []

    for i in range(0, len(nums)):
        arr.append(nums[i])
    for i in range(0, len(arr)):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr








# index0 = 0
# index1 = 1
# index2 = 2
# index3 = 3
#
# array("i", arr).swap(index0,index1)

# item_to_swap = arr.pop(index0)
# item_to_swap_2 = arr.pop(index2)
#
# arr.insert(index1, item_to_swap)
# arr.insert(index3, item_to_swap_2)





