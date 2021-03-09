import sys
from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def get_zero(graph, n, m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


def bfs(graph, starts, n, m):
    queue = deque()
    for start in starts:
        queue.append(start)
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # 인덱스 범위 밖
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽이거나 방문 이력 있음
            if graph[nx][ny] >= 1:
                continue
            graph[nx][ny] = 2
            queue.append((nx, ny))


def solution(graph, n, m):
    tmp_graph = copy.deepcopy(graph)
    starts = list()
    empty_space = list()
    answers = set()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                starts.append((i, j))
            if graph[i][j] == 0:
                empty_space.append((i, j))

    for i in range(len(empty_space)):
        for j in range(i+1, len(empty_space)):
            for k in range(j+1, len(empty_space)):
                graph = copy.deepcopy(tmp_graph)
                graph[empty_space[k][0]][empty_space[k][1]] = 1
                graph[empty_space[j][0]][empty_space[j][1]] = 1
                graph[empty_space[i][0]][empty_space[i][1]] = 1

                bfs(graph, starts, n, m)

                answers.add(get_zero(graph, n, m))
                graph[empty_space[k][0]][empty_space[k][1]] = 0
                graph[empty_space[j][0]][empty_space[j][1]] = 0
                graph[empty_space[i][0]][empty_space[i][1]] = 0

    answer = max(answers)
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    G = list()
    for _ in range(N):
        G.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(G, N, M))
