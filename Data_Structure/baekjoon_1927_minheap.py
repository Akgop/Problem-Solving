import sys
import heapq

N = int(sys.stdin.readline().rstrip())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, x)
