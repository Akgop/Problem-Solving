import sys


def dfs(depth, n, m, s):
    if depth == m:
        print(' '.join(map(str, li)))
        return
    for i in range(s, n):
        if visited[i] == 0:
            visited[i] = 1
            li.append(i+1)
            dfs(depth+1, n, m, i)
            li.pop()
            visited[i] = 0


N, M = map(int, sys.stdin.readline().split())
li = []
visited = [0] * N
dfs(0, N, M, 0)
