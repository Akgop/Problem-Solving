import sys


def dp(row, col):
    for i in range(1, col):
        for j in range(1, row):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]


t = int(sys.stdin.readline().rstrip())
apart = [[1] * 16 for _ in range(16)]
dp(15, 16)

for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(apart[k+1][n-1])

