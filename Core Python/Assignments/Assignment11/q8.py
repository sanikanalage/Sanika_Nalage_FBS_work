#Que8.Print 1 to 100 in snakes and ladder pattern.

li = list(range(1, 101))

for i in range(9, -1, -1):
    row = li[i * 10:(i + 1) * 10]

    if (9 - i) % 2 == 0:
        row.reverse()

    print(*row)