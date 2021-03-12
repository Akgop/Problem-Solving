import sys
import heapq

INF = int(1e9)


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for des, weight in adj_lst[now].items():
            cost = dist + weight
            if cost < distance[des]:
                distance[des] = cost
                heapq.heappush(q, (cost, des))


def solution(n, v1, v2):
    distance = [INF] * (n + 1)
    dijkstra(1, distance)
    one_to_v1 = distance[v1]
    one_to_v2 = distance[v2]

    distance = [INF] * (n + 1)
    dijkstra(v1, distance)
    v1_to_v2 = distance[v2]
    v1_to_n = distance[n]

    distance = [INF] * (n + 1)
    dijkstra(v2, distance)
    v2_to_v1 = distance[v1]
    v2_to_n = distance[n]

    # 사실 무방향 그래프 이므로 v1_to_v2 와 v2_to_v1은 동일하다.
    first_path = one_to_v1 + v1_to_v2 + v2_to_n
    second_path = one_to_v2 + v2_to_v1 + v1_to_n

    answer = min(first_path, second_path)
    if answer >= INF:
        answer = -1

    return answer


if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = [dict() for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        try:
            adj_lst[a][b] = min(adj_lst[a][b], c)
        except:
            adj_lst[a][b] = c
        try:
            adj_lst[b][a] = min(adj_lst[b][a], c)
        except:
            adj_lst[b][a] = c
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    print(solution(N, v1, v2))
