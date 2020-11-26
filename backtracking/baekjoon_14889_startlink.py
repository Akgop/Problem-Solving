import sys


def cal(n):
    start = 0
    link = 0
    for e1 in range(n):
        for e2 in range(e1, n):
            if visited[e1] is True and visited[e2] is True:
                start += S[e1][e2] + S[e2][e1]
            elif visited[e1] is False and visited[e2] is False:
                link += S[e1][e2] + S[e2][e1]
    result.append(abs(start - link))


def dfs(depth, n, s):
    if depth == n//2:
        cal(n)
        return
    for i in range(s, n):
        if visited[i] is False:
            visited[i] = True
            dfs(depth+1, n, i)
            visited[i] = False


S = []
N = int(input())
visited = [False] * N
result = []
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))
dfs(0, N, 0)
print(min(result))
