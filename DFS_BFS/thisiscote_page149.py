import sys


def dfs(x, y):
    # 인덱스를 벗어 났으면 (배열 인덱스 주의)
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    # 현재 노드는 방문으로 표시
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 모두 각각 재귀
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


N, M = map(int, sys.stdin.readline().split())
graph = list()
for i in range(N):
    # readline 사용 시 rstrip 을 사용하여 \n을 제거한다
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 탐색 시작
answer = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) is True:
            answer += 1
print(answer)

