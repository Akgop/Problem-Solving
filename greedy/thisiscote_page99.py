import sys

N, K = map(int, sys.stdin.readline().split())
count = 0
while N != 1:
    if N % K == 0:
        N = N // K
    else:
        N -= 1
    count += 1
print(count)

N, K = map(int, sys.stdin.readline().split())
count = 0
while N >= K:
    if N % K == 0:
        N = N // K
        count += 1
    else:
        tmp = (N // K) * K
        count += (N - tmp)
        N = tmp
count += (N - 1)
print(count)
