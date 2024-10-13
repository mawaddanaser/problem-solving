allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

count = 0

for i in allowed:
    for word in words:
        if words[i] in allowed:
            count += 1
print(count)