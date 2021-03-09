import sys


def dfs(depth, n, m, s):
    if depth == m:
        print(' '.join(map(str, li)))
        return
    for i in range(s, n):
        li.append(i+1)
        dfs(depth+1, n, m, i)
        li.pop()


N, M = map(int, sys.stdin.readline().split())
li = []
dfs(0, N, M, 0)
