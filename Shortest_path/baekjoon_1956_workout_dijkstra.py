import sys
import heapq


def dijkstra(n, start):
    dist = [INF] * (n+1)
    heap = []

    for node, cost in edge[start].items():
        heapq.heappush(heap, (cost, node))
        dist[node] = cost

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_node == start:
            return dist[cur_node]
        if dist[cur_node] < cur_dist:
            continue
        for to_node, to_dist in edge[cur_node].items():
            if dist[cur_node] + to_dist < dist[to_node]:
                dist[to_node] = dist[cur_node] + to_dist
                heapq.heappush(heap, (dist[to_node], to_node))
    return INF


def solution(n):
    answer = INF
    for i in range(1, n+1):
        answer = min(dijkstra(n, i), answer)
    return answer if answer < INF else -1


if __name__ == "__main__":
    INF = int(1e9)
    V, E = map(int, sys.stdin.readline().rstrip().split())
    edge = [dict() for _ in range(V+1)]
    for _ in range(E):
        A, B, Cost = map(int, sys.stdin.readline().rstrip().split())
        edge[A][B] = Cost
    print(solution(V))
