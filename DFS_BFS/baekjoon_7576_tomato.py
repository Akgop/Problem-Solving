import sys
from collections import deque

dx = [1, -1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]


def get_max(graph):
    _max = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            if _max < graph[i][j]:
                _max = graph[i][j]
    return _max - 1


def bfs(graph, start, n, m):
    queue = deque()
    for c in start:
        queue.append(c)   # 세로, 가로, 거리(깊이)
    while queue:
        cur_x, cur_y, depth = queue.popleft()
        # 네 방향 탐색
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # 인덱스 범위 밖이면
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 토마토가 없는 공간이라면
            if graph[nx][ny] == -1:
                continue
            # 이미 방문했던 토마토라면
            if graph[nx][ny] > 1:
                # 지금 상황이 해당 토마토 밭에 더 가까우면
                if graph[nx][ny] > depth + 1:
                    graph[nx][ny] = depth + 1
                    queue.append((nx, ny, depth + 1))
            # 처음 방문하는 토마토라면
            if graph[nx][ny] == 0:
                graph[nx][ny] = depth + 1
                queue.append((nx, ny, depth + 1))


def solution(graph, n, m):
    start = list()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:    # (n, m)
                start.append((i, j, 1))
    bfs(graph, start, n, m)
    answer = get_max(graph)
    return answer


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().rstrip().split())
    G = list()
    for _ in range(N):
        G.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(G, N, M))
