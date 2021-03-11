import sys
from collections import deque

move = [
    (-1, -2), (-2, -1), (-2, 1), (-1, 2),
    (1, -2), (2, -1), (2, 1), (1, 2)
]


def bfs(start, target, length):
    q = deque()
    q.append(start)
    visited = [[False]*length for _ in range(length)]
    visited[start[0]][start[1]] = True
    while q:
        cur = q.popleft()
        # 원하는 위치 도착
        if cur[0] == target[0] and cur[1] == target[1]:
            return cur[2]
        # 8방향 탐색
        for x, y in move:
            nx = cur[0] + x
            ny = cur[1] + y
            # 인덱스 벗어남
            if nx < 0 or ny < 0 or nx >= length or ny >= length:
                continue
            # 방문했었음
            if visited[nx][ny] is True:
                continue
            # 이동
            q.append((nx, ny, cur[2] + 1))
            visited[nx][ny] = True


def solution(start, target, length):
    x, y = start
    return bfs((x, y, 0), target, length)


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        L = int(sys.stdin.readline().rstrip())
        graph = [[False] * L for _ in range(L)]
        S = list(map(int, sys.stdin.readline().rstrip().split()))
        T = list(map(int, sys.stdin.readline().rstrip().split()))
        print(solution(S, T, L))
