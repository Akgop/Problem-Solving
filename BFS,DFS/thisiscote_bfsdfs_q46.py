import sys
from collections import deque
import heapq

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(start, n, size):
    heap = []
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True
    dist = 0
    while q:
        x, y, dist = q.popleft()
        if heap:
            if heap[0][0] < dist:
                dist, x, y = heapq.heappop(heap)
                graph[x][y] = 0
                return x, y, dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위 밖
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 벽(숫자가 큰 물고기만남)
            if graph[nx][ny] > size:
                continue
            # 이미 방문한 공간
            if visited[nx][ny]:
                continue
            # 더 작은 물고기를 만남 -> 먹잇감으로 지정
            if 0 < graph[nx][ny] < size:
                heapq.heappush(heap, (dist + 1, nx, ny))
            # 그냥 이동 경로임
            q.append((nx, ny, dist+1))
            visited[nx][ny] = True
    if heap:
        dist, x, y = heapq.heappop(heap)
        graph[x][y] = 0
        return x, y, dist
    return -1, -1, 0


def solution(n):
    # 초기 변수들 설정
    size = 2
    count = 0
    time = 0

    # 상어 위치 찾음
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                start_x, start_y = i, j

    # 상어가 엄마를 찾을 때 까지 반복
    while True:
        next_x, next_y, spent_time = bfs((start_x, start_y), n, size)
        graph[start_x][start_y] = 0
        # 엄마 상어 찾음
        if next_x == -1 and next_y == -1:
            break
        start_x, start_y = next_x, next_y
        time += spent_time
        count += 1      # 먹은 횟수 + 1
        if count == size:   # 상어의 크기 + 1
            count = 0
            size += 1
    return time


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N))
