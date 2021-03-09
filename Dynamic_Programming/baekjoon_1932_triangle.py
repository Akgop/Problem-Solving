import sys

N = int(input())
t = list()
first = int(input())
if N == 1:
    print(first)
else:
    for i in range(0, N-1):
        t.append(list(map(int, sys.stdin.readline().split())))
    result = [0] * N
    for i in range(N-3, -1, -1):
        for j in range(0, len(t[i])):
            result[j] = max(t[i+1][j], t[i+1][j+1])
        for j in range(0, len(t[i])):
            t[i][j] = t[i][j] + result[j]
    print(first + max(t[0]))
