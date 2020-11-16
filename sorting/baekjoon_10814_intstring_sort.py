import sys

N = int(sys.stdin.readline())
mem = []
for _ in range(N):
    a, n = sys.stdin.readline().split()
    mem.append([a, n])
result = sorted(mem, key=lambda x: int(x[0]))
for i in range(N):
    print(' '.join(result[i]))
