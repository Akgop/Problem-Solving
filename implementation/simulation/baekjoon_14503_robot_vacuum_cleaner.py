import sys
from pprint import pprint

dr = [-1, 0, 1, 0]  # 북0 동1 남2 서3
dc = [0, 1, 0, -1]  # 북0 동1 남2 서3


def turn_left(di):
    di -= 1
    if di == -1:
        di = 3
    return di


def solution(r, c, d):
    answer = 1
    turn_count = 0
    visited[r][c] = 1
    while True:
        # Step 2
        d = turn_left(d)  # 왼쪽 탐색
        nr = r + dr[d]
        nc = c + dc[d]
        # Step 2-a
        if table[nr][nc] == 0 and visited[nr][nc] == 0:  # 청소하지 않은 공간
            # Step 1 현위치 청소
            visited[nr][nc] = 1
            turn_count = 0
            answer += 1
            r = nr
            c = nc
            continue
        else:
            turn_count += 1
        # Step 2-c 후진 조건
        if turn_count == 4:
            nr = r - dr[d]
            nc = c - dc[d]
            # Step 2-d 종료 조건
            if table[nr][nc] == 1:
                break
            r = nr
            c = nc
            turn_count = 0
    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
R, C, D = map(int, sys.stdin.readline().rstrip().split())
table = []
visited = [[0] * M for _ in range(N)]
for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(R, C, D))
