import sys
import heapq


def solution(n, start, cost_limit):
    dist_dp = [INF] * (n+1)
    cost_dp = [INF] * (n+1)
    heap = []
    heapq.heappush(heap, (0, 0, start))
    answer = INF
    while heap:
        print(heap, dist_dp, cost_dp)
        cur_cost, cur_dist, cur_node = heapq.heappop(heap)
        if cur_node == n:
            answer = min(cur_dist, answer)
        # 비용과 거리 둘다 크다면 굳이 더 수행할 이유가 없음.
        if cur_cost > cost_dp[cur_node] and cur_dist > dist_dp[cur_node]:
            continue
        for to_node, to_cost, to_dist in routes[cur_node]:
            new_cost = cur_cost + to_cost
            new_dist = cur_dist + to_dist
            # 둘 다 크면 해당 경로를 굳이 해볼 이유가 없음. -> worst case 에서는 의미 없음..
            if new_cost > cost_dp[to_node] and new_dist > dist_dp[to_node]:
                continue
            # 최소 비용을 넘어서면 해볼 이유가 없음
            if new_cost > cost_limit:
                continue
            # 아니라면
            cost_dp[to_node] = max(new_cost, cost_dp[to_node]) if cost_dp[to_node] != INF else new_cost
            dist_dp[to_node] = max(new_dist, dist_dp[to_node]) if dist_dp[to_node] != INF else new_dist
            heapq.heappush(heap, (new_cost, new_dist, to_node))
    return answer if answer != INF else "Poor KCM"


if __name__ == "__main__":
    INF = int(1e9)
    test_cases = int(sys.stdin.readline().rstrip())
    for _ in range(test_cases):
        N, M, K = map(int, sys.stdin.readline().rstrip().split())
        routes = [[] for _ in range(N + 1)]
        for _ in range(K):
            U, V, C, D = map(int, sys.stdin.readline().rstrip().split())
            routes[U].append([V, C, D])
        print(solution(N, 1, M))
