import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # items 쓸껄..
        for adj in adj_lst[now].keys():
            cost = dist + adj_lst[now][adj]
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))


def solution(vtx, k):
    dijkstra(k)
    for i in range(1, vtx + 1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().rstrip().split())
    K = int(sys.stdin.readline().rstrip())
    adj_lst = [{} for _ in range(V + 1)]
    distance = [INF] * (V + 1)
    for _ in range(E):
        u, v, Cost = map(int, sys.stdin.readline().rstrip().split())
        try:
            adj_lst[u][v] = min(adj_lst[u][v], Cost)
        except:
            adj_lst[u][v] = Cost
    solution(V, K)
