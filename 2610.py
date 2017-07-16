matrix = []
user_input = input()
while user_input != 'end':
    user_input = [int(i) for i in user_input.split()]
    matrix.append(user_input)
    user_input = input()
for i in range(len(matrix)):
    print()
    for j in range(len(matrix[0])):
        print(matrix[i - 1][j] + matrix[i + 1 - len(matrix)][j] + matrix[i][j - 1] + matrix[i][j + 1 - len(matrix[0])], end=' ')

