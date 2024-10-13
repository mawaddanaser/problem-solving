gain = [-5,1,5,0,-7]

altitude = [0]
for i in range(0, len(gain) -1):
    altitude += gain[i] + gain[i + 1]
print(altitude)