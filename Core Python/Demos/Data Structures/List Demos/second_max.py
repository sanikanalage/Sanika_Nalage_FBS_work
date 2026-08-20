li = [64, 50,92,14,52,96]

max = li[0]
second_max = li[0]

for ind in range(1, len(li)):
    if li[ind] > max:
        second_max = max
        max = li[ind]
    elif li[ind] > second_max:
        second_max = li[ind]

print("Maximum Element:", max)
print("Second Maximum Element:", second_max)