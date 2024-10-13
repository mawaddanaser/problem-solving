nums = [4, 5, 2, 1]
queries = [3, 10, 21]

answer = [None] * len(queries)
sum = 0


for i in range(0, len(queries)):
    count = 0
    for j in nums:
        sum += j
        if queries[i] <= sum:
            answer.append(sum)
print(answer)