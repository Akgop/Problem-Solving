import sys
from collections import deque


def bfs(home_cnt):
    visited = set()
    que = deque()
    for f in fountain:
        que.append([f, 0])
        visited.add(f)

    answer = 0
    while True:
        cur, dist = que.popleft()
        for i in range(2):
            nxt = cur + dx[i]
            cost = dist + 1
            if nxt in visited:
                continue
            answer += cost
            home_cnt -= 1
            if home_cnt == 0:
                return answer
            que.append([nxt, cost])
            visited.add(nxt)


if __name__ == "__main__":
    MIN, MAX = -int(1e8), int(1e8)
    N, K = map(int, sys.stdin.readline().rstrip().split())
    fountain = list(map(int, sys.stdin.readline().rstrip().split()))
    dx = [-1, 1]
    print(bfs(K))
