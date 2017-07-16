figure = int(input())
counter = 0
for i in range(1, figure + 1):
    for j in range(1, i + 1):
        if counter == figure:
            break
        print(i, end=' ')
        counter += 1

