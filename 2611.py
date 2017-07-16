n = int(input())
matrix = [[0] * n for i in range(n)]
counter = 0
i = 0
j = 0
level = 0
while counter < n ** 2:
    counter += 1
    matrix[i][j] = counter
    if i == level + 1 and j == level:
        level += 1
    if i == level and j < n - level - 1:
        j += 1
    elif j == n - level - 1 and i < n - level - 1:
        i += 1
    elif i == n - level - 1 and j > level:
        j -= 1
    elif j == level and i > level:
        i -= 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


