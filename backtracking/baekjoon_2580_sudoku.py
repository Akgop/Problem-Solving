# Thanks to "coreenee.github.io/2020/01/23/"
import sys


def dfs(depth):
    if depth == len(empty_co):
        for q in range(9):
            print(' '.join(map(str, matrix[q])))
        sys.exit()      # pypy3이므로
    row, col = empty_co[depth]
    num_list = [True] * 10
    num_list[0] = False
    for i in range(9):
        if matrix[i][col] != 0:
            num_list[matrix[i][col]] = False
        if matrix[row][i] != 0:
            num_list[matrix[row][i]] = False
    for i in range((row//3)*3, (row//3)*3 + 3):
        for j in range((col//3)*3, (col//3)*3 + 3):
            if matrix[i][j] != 0:
                num_list[matrix[i][j]] = False
    available_list = [i for i, s in enumerate(num_list) if s is True]
    for i in available_list:
        matrix[row][col] = i
        dfs(depth + 1)
        matrix[row][col] = 0


matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))
empty_co = [(i, j) for i in range(0, 9) for j in range(0, 9) if matrix[i][j] == 0]
dfs(0)



