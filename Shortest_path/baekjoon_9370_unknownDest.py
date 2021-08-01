import sys
import heapq


def dijkstra(n, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, cur = heapq.heappop(heap)
        if cost > dist[cur]:
            continue
        for adj_node, adj_cost in adj_lst[cur].items():
            if adj_cost + dist[cur] < dist[adj_node]:
                dist[adj_node] = adj_cost + dist[cur]
                heapq.heappush(heap, (adj_cost + dist[cur], adj_node))
    return dist


def solution(n, start, must_pass1, must_pass2):
    dist_from_start = dijkstra(n, start)
    if dist_from_start[must_pass1] < dist_from_start[must_pass2]:
        near, far = must_pass1, must_pass2
    else:
        near, far = must_pass2, must_pass1
    dist_from_far = dijkstra(n, far)

    result = []
    for target in targets:
        if dist_from_start[target] == (dist_from_start[near] + adj_lst[near][far] + dist_from_far[target]):
            result.append(target)
    result.sort()
    print(' '.join(str(x) for x in result))


if __name__ == "__main__":
    INF = int(1e9)
    test_cases = int(sys.stdin.readline().rstrip())
    for _ in range(test_cases):
        N, M, T = map(int, sys.stdin.readline().rstrip().split())
        S, G, H = map(int, sys.stdin.readline().rstrip().split())
        adj_lst = [dict() for _ in range(N+1)]
        targets = []
        for _ in range(M):
            A, B, D = map(int, sys.stdin.readline().rstrip().split())
            adj_lst[A][B] = D
            adj_lst[B][A] = D
        for _ in range(T):
            targets.append(int(sys.stdin.readline().rstrip()))
        solution(N, S, G, H)
