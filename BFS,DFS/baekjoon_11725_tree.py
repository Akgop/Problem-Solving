import sys
from collections import deque


def bfs(n):
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        cur = q.popleft()
        for node in tree[cur]:
            # 이미 방문했던 상위 노드라면
            if visited[node]:
                continue
            parent[node] = cur
            visited[node] = True
            q.append(node)
    for i in range(2, n + 1):
        print(parent[i])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        tree[a].append(b)
        tree[b].append(a)
    bfs(N)
