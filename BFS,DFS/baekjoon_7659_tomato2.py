import sys
from collections import deque

dx = [0, 0, 1, -1, 0, 0]  # 위, 아래, 상, 하, 좌, 우
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]


def get_max(graph, m, n, h):
    _max = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
                if _max < graph[i][j][k]:
                    _max = graph[i][j][k]
    return _max - 1


def bfs(graph, starts, m, n, h):
    queue = deque()
    for start in starts:
        queue.append(start)
    while queue:
        # 높이, 세로, 가로, 출발거리
        cur_z, cur_x, cur_y, depth = queue.popleft()
        for i in range(6):
            nz = cur_z + dz[i]
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # 인덱스 범위 밖
            if nz < 0 or nx < 0 or ny < 0 or nz >= h or nx >= n or ny >= m:
                continue
            # -1인 경우
            if graph[nz][nx][ny] == -1:
                continue
            # 이미 지나온 길
            if graph[nz][nx][ny] > 1:
                # 지금 내가 더 짧은 길로 왔으면
                if graph[nz][nx][ny] > depth + 1:
                    graph[nz][nx][ny] = depth + 1
                    queue.append((nz, nx, ny, depth + 1))
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = depth + 1
                queue.append((nz, nx, ny, depth + 1))


def solution(graph, m, n, h):
    starts = list()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    starts.append((i, j, k, 1))
    bfs(graph, starts, m, n, h)
    answer = get_max(graph, m, n, h)
    return answer


if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().rstrip().split())
    G = list()
    for _ in range(H):
        tmp_G = list()
        for _ in range(N):
            tmp_G.append(list(map(int, sys.stdin.readline().rstrip().split())))
        G.append(tmp_G)
    print(solution(G, M, N, H))
