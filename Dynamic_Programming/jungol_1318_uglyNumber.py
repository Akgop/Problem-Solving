import sys
import heapq


def solution(m):
    calc = [2, 3, 5]
    heap = []
    for c in calc:
        heapq.heappush(heap, c)
        c_set.add(c)
    cur = 0
    while cur <= m:
        cur = heapq.heappop(heap)
        cache.append(cur)
        for dc in calc:
            if cur * dc in c_set:
                continue
            heapq.heappush(heap, cur * dc)
            c_set.add(cur * dc)


if __name__ == "__main__":
    cache = [1]
    c_set = {1}
    MAX = int(1e9)
    solution(MAX)
    while True:
        N = int(sys.stdin.readline().rstrip())
        if N == 0:
            break
        print(cache[N-1])  # N번째 못생긴 수
