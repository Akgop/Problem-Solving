import sys
import heapq
from collections import deque

def solution(n, k):
    visited = [False] * MAX
    hq = []
    heapq.heappush(hq, (0, n))
    visited[n] = True
    while hq:
        time, cur = heapq.heappop(hq)
        if cur == k:
            return time
        # 1. n의 배수 전부다 time 그대로 해서 queue 에 넣음
        if 2*cur < MAX and not visited[2*cur]:
            heapq.heappush(hq, (time, 2*cur))
            visited[2*cur] = True
        # 2. 자신 좌우 넣음
        if cur+1 < MAX and not visited[cur+1]:
            heapq.heappush(hq, (time+1, cur+1))
            visited[cur+1] = True
        if cur-1 > MIN and not visited[cur-1]:
            heapq.heappush(hq, (time+1, cur-1))
            visited[cur-1] = True
    return -1


def solution2(n, k):
    visited = [False] * MAX
    que = deque()
    que.append((n, 0))
    visited[n] = True
    while que:
        cur, time = que.popleft()
        if cur == k:
            return time
        # 1. n의 배수 전부다 time 그대로 해서 queue에 넣음
        nxt = cur*2
        while nxt < MAX and nxt != 0:
            if not visited[nxt]:
                que.append((nxt, time))
                visited[nxt] = True
            nxt *= 2
        # 2. 자신 좌우 넣음
        if cur + 1 < MAX and not visited[cur + 1]:
            que.append((cur + 1, time + 1))
            visited[cur + 1] = True
        if cur - 1 > MIN and not visited[cur - 1]:
            que.append((cur - 1, time + 1))
            visited[cur - 1] = True
    return -1


if __name__ == "__main__":
    MIN, MAX = -1, 100001
    N, K = map(int, sys.stdin.readline().split())
    print(solution(N, K))
