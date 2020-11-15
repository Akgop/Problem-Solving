import sys


def fibonacci(n, c):
    if n == 0:
        c[0] = 0
        return c[0]
    elif n == 1:
        c[1] = 1
        return c[1]
    else:
        if c[n-1] == -1:
            c[n-1] = fibonacci(n-1, c)
        if c[n-2] == -1:
            c[n-2] = fibonacci(n-2, c)
        return c[n-1] + c[n-2]


T = int(sys.stdin.readline())
C = [-1]*40
for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fibonacci(N-1, C), fibonacci(N, C))
