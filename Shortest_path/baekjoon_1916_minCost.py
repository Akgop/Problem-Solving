import sys
import heapq


def dijkstra(start, dest, n):
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for to, length in adj_lst[node]:
            if dist[node] + length < dist[to]:
                dist[to] = dist[node] + length
                heapq.heappush(heap, (dist[to], to))
    return dist[dest]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    adj_lst = [[] for _ in range(N+1)]
    INF = int(1e9)
    for _ in range(M):
        _start, _end, _cost = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[_start].append([_end, _cost])
    S, D = map(int, sys.stdin.readline().rstrip().split())
    print(dijkstra(S, D, N))
