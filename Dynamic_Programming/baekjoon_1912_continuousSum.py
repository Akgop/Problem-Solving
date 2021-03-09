import sys
N = int(input())
li = list(map(int, sys.stdin.readline().split()))
N_INF = -1001
result = [N_INF]*N
result[0] = li[0]
for i in range(1, N):
    if result[i-1] + li[i] >= 0:
        result[i] = max(result[i-1] + li[i], li[i])
    else:
        result[i] = li[i]
print(max(result))
