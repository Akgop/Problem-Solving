import sys


def dfs(g, x, y):
    # 인덱스 범위 밖
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    # 이미 방문 했거나 배추가 없는 곳
    if g[y][x] == 0:
        return False
    # 방문 표시 -> 상하좌우
    g[y][x] = 0
    dfs(g, x - 1, y)
    dfs(g, x + 1, y)
    dfs(g, x, y + 1)
    dfs(g, x, y - 1)
    return True


sys.setrecursionlimit(10000)
T = int(sys.stdin.readline().rstrip())
# 테스트 케이스만큼 반복
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1
    for i in range(M):   # x
        for j in range(N):  # y
            if dfs(graph, i, j) is True:
                answer += 1
    print(answer)
