import sys
from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(starts, n, m):
    q = deque()
    visited = [[False] * m for _ in range(n)]
    for start in starts:
        q.append(start)
        visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 아웃, 이미 방문
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            # 벽이거나 바이러스가 있거나
            if graph[nx][ny] >= 1:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))

    answer = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                answer += 1
    return answer


def solution(n, m):
    virus = []
    empty = []
    # 바이러스와 빈 공간을 세어줌
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                virus.append((i, j))
            elif graph[i][j] == 0:
                empty.append((i, j))
    # eC3
    cases = combinations(empty, 3)

    # 브루트포스
    answer = 0
    for case in cases:
        # 벽 침
        for c in case:
            graph[c[0]][c[1]] = 1
        answer = max(answer, bfs(virus, n, m))
        # 벽 회수
        for c in case:
            graph[c[0]][c[1]] = 0
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, M))
