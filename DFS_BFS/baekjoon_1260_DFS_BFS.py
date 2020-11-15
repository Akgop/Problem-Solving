import sys


def dfs(root):
    visited[root] = 1
    print(root, end=' ')
    for j in range(1, N+1):
        if visited[j] == 0 and graph[root][j] == 1:
            dfs(j)


def bfs(root):
    queue = [root]
    visited[root] = 0
    while queue:
        root = queue.pop(0)
        print(root, end=' ')
        for j in range(1, N+1):
            if visited[j] == 1 and graph[root][j] == 1:
                queue.append(j)
                visited[j] = 0


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s][e] = graph[e][s] = 1
dfs(V)
print()
bfs(V)
