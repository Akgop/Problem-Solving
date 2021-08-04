import sys
import heapq


def solution(n, start, cost_limit):
    # 행은 노드 번호 열은 비용
    dp = [[INF] * (cost_limit+1) for _ in range(n+1)]
    dp[1][0] = 0    # 1에서 1로 가는 비용은 0
    heap = []
    heapq.heappush(heap, (0, 0, start))
    answer = INF
    while heap:
        cur_dist, cur_cost, cur_node = heapq.heappop(heap)
        if cur_dist > dp[cur_node][cur_cost]:
            continue
        # 비용에 구애받지 않고 최단 거리로(heap 에 의해 보장) n에 도달한 경우 stop
        if cur_node == n:
            answer = cur_dist
            break
        for to_cost, to_dist, to_node in routes[cur_node]:
            new_cost = cur_cost + to_cost
            new_dist = cur_dist + to_dist
            # 만약 new cost 가 cost limit 을 넘기면 pass
            if new_cost > cost_limit:
                continue
            # heap 에 굳이 넣을 이유가 없다면 pass
            if dp[to_node][new_cost] <= new_dist:
                continue
            # dp table 값을 업데이트 해야함
            for i in range(new_cost, cost_limit + 1):
                if dp[to_node][i] < new_dist:
                    break
                dp[to_node][i] = new_dist
            heapq.heappush(heap, (new_dist, new_cost, to_node))
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
