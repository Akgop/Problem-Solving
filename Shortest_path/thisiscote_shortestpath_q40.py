import heapq


def solution(n, m, links):
    inf = int(1e9)

    # result list
    dist = [inf] * (n+1)

    # adjacency list - bi-direction
    adj_lst = [[] for _ in range(n+1)]
    for src, des in links:
        adj_lst[src].append([des, 1])
        adj_lst[des].append([src, 1])

    # dijkstra
    hq = []
    dist[1] = 0
    heapq.heappush(hq, (0, 1))
    while hq:
        d, v = heapq.heappop(hq)
        if dist[v] < d:
            continue
        for adj in adj_lst[v]:
            cost = adj[1] + d
            if cost < dist[adj[0]]:
                dist[adj[0]] = cost
                heapq.heappush(hq, (cost, adj[0]))

    _max = max(dist[1:])
    answer = ' '.join(map(str, [dist.index(_max), _max, dist.count(_max)]))
    return answer



print(solution(
    6, 7, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
))