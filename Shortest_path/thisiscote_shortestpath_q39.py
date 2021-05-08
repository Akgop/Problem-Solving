import heapq


def solution(n, spaces):
    inf = int(1e9)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[inf] * n for _ in range(n)]
    hq = []

    # 시작점 초기화
    heapq.heappush(hq, (spaces[0][0], 0, 0))
    while hq:
        d, x, y = heapq.heappop(hq)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스 범위 밖
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = d + spaces[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heapq.heappush(hq, (cost, nx, ny))
    return dist[n-1][n-1]


print(solution(
    3, [[5, 5, 4], [3, 9, 1], [3, 2, 7]]
))

print(solution(
    5,
    [[3, 7, 2, 0, 1],
     [2, 8, 0, 9, 1],
     [1, 2, 1, 8, 1],
     [9, 8, 9, 2, 0],
     [3, 6, 5, 1, 5]]
))

print(solution(
    7, [[9, 0, 5, 1, 1, 5, 3],
        [4, 1, 2, 1, 6, 5, 3],
        [0, 7, 6, 1, 6, 8, 5],
        [1, 1, 7, 8, 3, 2, 3],
        [9, 4, 0, 7, 6, 4, 1],
        [5, 8, 3, 2, 4, 8, 3],
        [7, 4, 8, 4, 8, 3, 4]]
))