array = [64, 25, 12, 22, 11]


def selection_sort(array):
    for i in range(len(array)):
        # Find min element in unsorted part
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]
    return array


sorted_array = selection_sort(array)
print(f"Sorted Array is: {sorted_array}")
