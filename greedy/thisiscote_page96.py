import sys

N, M = map(int, sys.stdin.readline().split())
answer = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    row_min = min(row)
    answer = max(answer, row_min)
print(answer)
