import sys
import heapq

N = int(sys.stdin.readline().rstrip())
q = list()
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        print(-heapq.heappop(q) if q else 0)
    else:
        heapq.heappush(q, -x)
