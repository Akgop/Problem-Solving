import sys
from collections import deque

dx = [1, -1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def bfs(graph, x, y, r, c, dist):
    queue = deque()
    queue.append((x, y, dist))
    visited[x][y] = True
    result = -1
    while queue:
        tmp = queue.popleft()
        if tmp[0] == r and tmp[1] == c:  # 위치 도달
            result = tmp[2]
            break
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            # 인덱스를 벗어났다면
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            # 이동할 수 없는 칸이라면
            if graph[nx][ny] == 0:
                continue
            # 방문한 칸이라면
            if visited[nx][ny] is True:
                continue
            # 갈 수 있는 길이라면
            queue.append((nx, ny, tmp[2] + 1))  # 거리 + 1
            graph[nx][ny] = tmp[2] + 1
            visited[nx][ny] = True
    return result


def solution(g, n, m):
    answer = bfs(g, 0, 0, n-1, m-1, 1)
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    G = list()
    for _ in range(N):
        G.append(list(map(int, sys.stdin.readline().rstrip())))
    visited = [[False] * len(G[0]) for _ in range(len(G))]
    print(solution(G, N, M))
