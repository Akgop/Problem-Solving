import sys
from collections import deque
import copy


dn = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dm = [0, 0, -1, 1]


def bfs(tmp_graph, start, n, m):
    queue = deque()
    queue.append(start)
    tmp_graph[0][0] = 1
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while queue:
        now = queue.popleft()
        depth = now[2]
        for i in range(4):
            nn = now[0] + dn[i]
            nm = now[1] + dm[i]
            # 인덱스 벗어난 경우
            if nn < 0 or nm < 0 or nn >= n or nm >= m:
                continue
            # 이미 방문했던 노드 or 벽
            if visited[nn][nm] is True or tmp_graph == 1:
                continue
            # queue 에 넣고 방문 처리
            queue.append((nn, nm, depth + 1))
            tmp_graph[nn][nm] = depth + 1


def solution(n, m):
    tmp_graph = copy.deepcopy(graph)
    bfs(tmp_graph, (0, 0, 1), n, m)

    # 벽만 모아놓은 리스트 생성: O(NM): 100만
    walls = list()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                walls.append((i, j))




if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
    solution(N, M)
