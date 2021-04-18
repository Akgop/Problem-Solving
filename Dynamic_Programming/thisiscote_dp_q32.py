import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
dp = [[0] * (N+2) for _ in range(N)]

dp[0][1] = int(sys.stdin.readline().rstrip())

for i in range(1, N):
    q = deque(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(1, i + 2):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + q.popleft()

print(max(dp[N-1]))


