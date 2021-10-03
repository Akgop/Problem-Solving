import sys
from collections import deque


def bfs(max_dist, start_video, n):
    visited = [False] * (n+1)
    que = deque()
    que.append(start_video)
    visited[start_video] = True
    count = 0
    while que:
        cur = que.popleft()
        for nxt, nxt_dist in usado[cur]:
            if visited[nxt] or nxt_dist < max_dist:
                continue
            count += 1
            que.append(nxt)
            visited[nxt] = True
    return count


if __name__ == "__main__":
    N, Q = map(int, sys.stdin.readline().split())
    usado = [[] for _ in range(N+1)]
    for _ in range(N-1):
        p, q, r = map(int, sys.stdin.readline().split())
        usado[p].append([q, r])
        usado[q].append([p, r])
    for _ in range(Q):
        k, v = map(int, sys.stdin.readline().split())
        print(bfs(k, v, N))
