import sys
N = int(input())
R = [0] * N
G = [0] * N
B = [0] * N
c = [[0] * 3 for _ in range(N)]
for i in range(N):
    R[i], G[i], B[i] = map(int, sys.stdin.readline().split())
c[0][0], c[0][1], c[0][2] = R[0], G[0], B[0]
for i in range(1, N):
    c[i][0] = min(R[i] + c[i - 1][1], R[i] + c[i - 1][2])
    c[i][1] = min(G[i] + c[i - 1][0], G[i] + c[i - 1][2])
    c[i][2] = min(B[i] + c[i - 1][0], B[i] + c[i - 1][1])
print(min(c[N-1]))

