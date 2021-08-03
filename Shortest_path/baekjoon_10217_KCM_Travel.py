import sys


def solution(n, cost_limit):
    # 행은 노드 번호 열은 비용
    dp = [[INF] * (cost_limit+1) for _ in range(n+1)]
    dp[1][0] = 0    # 1에서 1로 가는 비용은 0

    for cost in range(cost_limit+1):
        for node in range(1, n+1):
            if dp[node][cost] == INF:
                continue
            for to_cost, to_dist, to_node in routes[node]:
                new_cost = cost + to_cost
                new_dist = dp[node][cost] + to_dist
                if new_cost <= cost_limit:
                    dp[to_node][new_cost] = min(dp[to_node][new_cost], new_dist)
    return min(dp[n]) if min(dp[n]) != INF else "Poor KCM"


if __name__ == "__main__":
    INF = int(1e9)
    test_cases = int(sys.stdin.readline().rstrip())
    for _ in range(test_cases):
        N, M, K = map(int, sys.stdin.readline().rstrip().split())
        routes = [[] for _ in range(N + 1)]
        for _ in range(K):
            U, V, C, D = map(int, sys.stdin.readline().rstrip().split())
            routes[U].append([C, D, V])
        print(solution(N, M))