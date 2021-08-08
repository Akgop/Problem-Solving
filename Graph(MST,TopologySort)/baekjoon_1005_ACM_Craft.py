import sys
from collections import deque


def solution(target_w, n):
    que = deque()
    dp = [0] * (n + 1)
    # in degree 가 0인 노드를 start node로 설정
    for i in range(1, n+1):
        if not in_degree[i]:
            que.append(i)
            dp[i] = time[i]

    while que:
        cur_node = que.popleft()
        if cur_node == target_w:
            break
        for to_node in graph[cur_node]:
            # dp를 사용해서 더 오래걸리는 건물(경로)로 계속 업데이트
            dp[to_node] = max(dp[to_node], (dp[cur_node] + time[to_node]))
            in_degree[to_node] -= 1
            # in degree 가 0 인 노드를 queue 에 삽입
            if not in_degree[to_node]:
                que.append(to_node)
    return dp[target_w]


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().rstrip().split())
        time = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
        in_degree = [0] * (N + 1)
        graph = [[] for _ in range(N + 1)]
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().rstrip().split())
            graph[X].append(Y)
            in_degree[Y] += 1
        W = int(sys.stdin.readline().rstrip())
        print(solution(W, N))
