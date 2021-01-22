import sys
from pprint import pprint


def dfs(g, x, y, apt_n, cnt):
    # 인덱스 범위를 벗어났다면
    if x < 0 or y < 0 or x >= N or y >= N:
        return cnt
    # 이미 방문한 곳이거나 집이 없는 곳이라면
    if g[x][y] == 0 or g[x][y] > 1:
        return cnt
    # 아니라면 방문
    cnt += 1
    g[x][y] = apt_n
    cnt = dfs(g, x - 1, y, apt_n, cnt)
    cnt = dfs(g, x, y - 1, apt_n, cnt)
    cnt = dfs(g, x + 1, y, apt_n, cnt)
    cnt = dfs(g, x, y + 1, apt_n, cnt)
    return cnt


N = int(sys.stdin.readline().rstrip())
graph = list()
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
answer = 0
result = list()
apt_num = 2
count = 0
for i in range(N):
    for j in range(N):
        count = dfs(graph, i, j, apt_num, count)
        if count > 0:
            result.append(count)
            answer += 1
            apt_num += 1
            count = 0
print(answer)
result.sort()
for e in result:
    print(e)
