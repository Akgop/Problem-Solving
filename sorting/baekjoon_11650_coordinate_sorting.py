import sys
N = int(input())

c = [([0] * 2) for _ in range(N)]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    c[i][0] = x
    c[i][1] = y
c.sort(key=lambda z: (z[0], z[1]))
for i in range(N):
    print(c[i][0], c[i][1])
