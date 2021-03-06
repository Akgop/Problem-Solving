import sys
import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for a in graph[now]:
            cost = dist + a[1]
            if cost < distance[a[0]]:
                distance[a[0]] = cost
                heapq.heappush(heap, (cost, a[0]))


def solution(start):
    dijkstra(start)
    _max_cnt = len(distance)
    _max_time = 0
    for d in distance:
        if d == INF:
            _max_cnt -= 1
        elif d > _max_time:
            _max_time = d
    print(_max_cnt-1, _max_time)


if __name__ == "__main__":
    N, M, C = map(int, sys.stdin.readline().rstrip().split())
    INF = 1001
    graph = [[] * (N + 1) for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for _ in range(M):
        X, Y, Z = map(int, sys.stdin.readline().rstrip().split())
        graph[X].append((Y, Z))
    solution(C)
