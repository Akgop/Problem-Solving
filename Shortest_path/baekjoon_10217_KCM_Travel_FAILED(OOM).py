import sys
import heapq


def solution(n, start, cost_limit):
    # 행은 노드 번호 열은 비용
    dp = [[INF] * (cost_limit+1) for _ in range(n+1)]
    dp[1][0] = 0    # 1에서 1로 가는 비용은 0
    heap = []
    for to_cost, to_dist, to_node in routes[start]:
        dp[to_node][to_cost] = to_dist
        heapq.heappush(heap, (to_cost, to_dist, to_node))
    while heap:
        cur_cost, cur_dist, cur_node = heapq.heappop(heap)
        if dp[cur_node][cur_cost] < cur_dist:
            continue
        for to_cost, to_dist, to_node in routes[cur_node]:
            new_cost = cur_cost + to_cost
            new_dist = cur_dist + to_dist
            if new_cost > cost_limit:
                continue
            if new_dist < dp[to_node][new_cost]:
                dp[to_node][new_cost] = new_dist
                heapq.heappush(heap, (new_cost, new_dist, to_node))
    answer = INF
    for c in dp[n]:
        answer = min(c, answer)
    return answer if answer != INF else "Poor KCM"


if __name__ == "__main__":
    INF = int(1e9)
    test_cases = int(sys.stdin.readline().rstrip())
    for _ in range(test_cases):
        N, M, K = map(int, sys.stdin.readline().rstrip().split())
        routes = [[] for _ in range(N + 1)]
        for _ in range(K):
            U, V, C, D = map(int, sys.stdin.readline().rstrip().split())
            routes[U].append([C, D, V])
        print(solution(N, 1, M))