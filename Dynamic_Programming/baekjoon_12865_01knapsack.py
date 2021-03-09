import sys

N, K = map(int, sys.stdin.readline().split())
# 1D Array Solution
c = [0] * (K+1)
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().split())
for i in range(N):
    for j in range(K, 1, -1):   # 뒤 부터 보는 이유
        if W[i] <= j:           # 앞 부터 보면 변화한 값이 영향을 주기 때문에
            c[j] = max(c[j], c[j-W[i]] + V[i])  # j-W[i] index 의 값이 이미 변해있으므로
print(c[-1])

# 2D Array Solution
c = [[0] * (K+1) for _ in range(N+1)]
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().split())
for i in range(1, N+1):
    for j in range(1, K+1):
        if W[i-1] <= j:
            c[i][j] = max(V[i-1] + c[i-1][j-W[i-1]], c[i-1][j])
        else:
            c[i][j] = c[i-1][j]
print(c[-1][-1])

