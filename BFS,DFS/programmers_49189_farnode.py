from collections import deque
import sys

def bfs(n, graph):
    visited = [False] * (n + 1)
    visited[1] = True
    que = deque()
    que.append([0, 1])
    dist, count = 0, 0
    while que:
        dist_from_1, node = que.popleft()
        if dist == dist_from_1:
            count += 1
        else:
            dist += 1
            count = 1
        for adj_node in graph[node]:
            if visited[adj_node]:
                continue
            visited[adj_node] = True
            que.append([dist_from_1 + 1, adj_node])
    return count


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    return bfs(n, graph)
