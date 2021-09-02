from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(place, start):
    que = deque()
    visited = [[False] * 5 for _ in range(5)]
    que.append([0, start[0], start[1]])
    visited[start[0]][start[1]] = True
    while que:
        dist, x, y = que.popleft()
        if dist == 2:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue
            # 거리 2 안에 사람 등장
            if place[nx][ny] == 'P':
                return False
            que.append([dist + 1, nx, ny])
            visited[nx][ny] = True
    return True


def solution(places):
    answer = []
    for place in places:
        starts = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    starts.append([i, j])
        result = 1
        for s in starts:
            if not bfs(place, s):
                result = 0
                break
        answer.append(result)
    return answer



print(solution(
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
