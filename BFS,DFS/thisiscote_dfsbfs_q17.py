import sys
from collections import deque

dx = [1, -1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def bfs(starts, s, x, y, n, k):
    q = deque()
    for start in starts:
        q.append(start)

    while q:
        now = q.popleft()

        # 만약 시간초가 다 되었다면 -> 종료조건
        if now[3] == s:
            break

        # 상하좌우 이동하며 탐색
        for i in range(4):
            nx = now[1] + dx[i]
            ny = now[2] + dy[i]
            # 인덱스 범위 초과
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 이미 바이러스 존재
            if graph[nx][ny] != 0:
                continue
            # 바이러스 전이
            q.append((now[0], nx, ny, now[3] + 1))
            graph[nx][ny] = now[0]

    print(graph[x-1][y-1])


def solution(n, s, x, y, k):
    starts = list()
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                # 값, 인덱스 x, y, 시간 초
                starts.append((graph[i][j], i, j, 0))
    # 바이러스 번호 기준 정렬
    starts.sort(key=lambda col: col[0])
    bfs(starts, s, x, y, n, k)


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    S, X, Y = map(int, sys.stdin.readline().rstrip().split())
    solution(N, S, X, Y, K)
