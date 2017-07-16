matrix = []
while True:
    user_input = [i for i in input().split()]
    if user_input[0] == 'end':
        break
    matrix.append(user_input)
# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         matrix[i][j] = int(matrix[i][j])

for i in range(len(matrix[0])):
    print()
    for j in range(len(matrix)):
        print(matrix[i - 1][j] + matrix[i + 1 - len(matrix)][j] + matrix[i][j - 1] + matrix[i][j + 1 - len(matrix[0])], end=' ')


# for i in range(len(matrix[0])):
#     print()
#     for j in range(len(matrix)):
#         print(matrix[i][j], end=' ')

