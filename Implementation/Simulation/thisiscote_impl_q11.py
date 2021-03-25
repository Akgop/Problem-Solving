import sys
from collections import deque


dr = [-1, 0, 1, 0]  # 위 오른 아래 왼
dc = [0, 1, 0, -1]


def rotate(direction, c):
    if c == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    else:
        direction += 1
        if direction == 4:
            direction = 0
    return direction


def solution(n):
    # 0. 초기 설정
    count = 0
    d = 1  # 처음은 오른쪽 방향

    hr, hc = 0, 0
    q = deque()
    q.append((hr, hc))
    graph[hr][hc] = 2
    dist, direc = move.popleft()  # 하나 뺌
    while True:
        for i in range(count, dist):
            # 현재 방향으로 다음 위치 인덱스 구함
            next_hr = hr + dr[d]
            next_hc = hc + dc[d]
            # 벽을 만나면
            if next_hc < 0 or next_hr < 0 or next_hc >= n or next_hr >= n:
                return count + 1

            # 내 몸을 만나면
            if graph[next_hr][next_hc] == 2:
                return count + 1

            # 사과를 만나면
            if graph[next_hr][next_hc] == 1:    # 꼬리를 줄이지 않음
                pass
            # 아무 일도 없으면
            else:
                tail = q.popleft()       # 꼬리 줄이고
                graph[tail[0]][tail[1]] = 0

            graph[next_hr][next_hc] = 2
            q.append((next_hr, next_hc))
            hr, hc = next_hr, next_hc
            count += 1
        d = rotate(d, direc)
        try:
            dist, direc = move.popleft()  # 하나 뺌
        except:
            dist = 101      # 최대 값


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())
    graph = [[0]*N for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x-1][y-1] = 1
    L = int(sys.stdin.readline().rstrip())
    move = deque()
    for _ in range(L):
        a, b = map(str, sys.stdin.readline().rstrip().split())
        move.append((int(a), b))
    print(solution(N))
