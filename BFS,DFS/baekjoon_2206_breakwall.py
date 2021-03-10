import sys
from collections import deque
import copy


dn = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dm = [0, 0, -1, 1]


def bfs(start, n, m):
    q = deque()
    q.append(start)
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while q:
        now_x, now_y, wall = q.popleft()
        if now_x == n-1 and now_y == m-1:
            return visited[now_x][now_y][wall]
        for i in range(4):
            nn = now_x + dn[i]
            nm = now_y + dm[i]
            # 인덱스 벗어남
            if nn < 0 or nm < 0 or nn >= n or nm >= m:
                continue
            # 벽을 만나면 뚫고 차원이동, wall 이 0이라는 것은 아직 뚫지 않았다는 점
            if graph[nn][nm] == 1 and wall == 0:
                visited[nn][nm][1] = visited[now_x][now_y][0] + 1
                q.append((nn, nm, 1))
            # 그냥 일반 길을 만났을 때.
            if graph[nn][nm] == 0 and visited[nn][nm][wall] == 0:
                visited[nn][nm][wall] = visited[now_x][now_y][wall] + 1
                q.append((nn, nm, wall))
    return -1


def solution(n, m):
    answer = bfs((0, 0, 0), n, m)
    print(answer)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = list()
    walls = list()
    for idx in range(N):
        data = list(map(int, sys.stdin.readline().rstrip()))
        for idx2 in range(len(data)):
            if data[idx2] == 1:
                walls.append((idx, idx2))
        graph.append(data)
    solution(N, M)
