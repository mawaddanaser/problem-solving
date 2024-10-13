nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

res = []

for i in range(0, len(nums1)):
    for j in range(0, len(nums2)):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
        for k in res:
            pass
print(res)
