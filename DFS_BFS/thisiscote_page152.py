import sys
from collections import deque


# 방향을 골라서 움직여야 할 때 리스트형태로 사용
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # queue 가 비어있을 때까지
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위 밖이라면
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 괴물이 있거나 방문 이력이 있거나
            if graph[nx][ny] == 0 or graph[nx][ny] > 1:
                continue
            # 갈 수 있는 길이라면
            queue.append((nx, ny))   # 큐에 삽입
            graph[nx][ny] = graph[x][y] + 1
    return graph[-1][-1]


N, M = map(int, sys.stdin.readline().split())
graph = list()
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
print(bfs(0, 0))
