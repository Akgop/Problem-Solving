import sys
from collections import deque


def bfs(visited, start):
    que = deque()
    que.append(start)
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append(nxt)
    return visited


def solution(n, m):
    visited = [False] * (n+1)
    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            bfs(visited, i)
            count += 1
    return count


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        frm, to = map(int, sys.stdin.readline().split())
        graph[frm].append(to)
        graph[to].append(frm)
    print(solution(N, M))
