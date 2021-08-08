import sys
from collections import deque


def solution(n):
    answer = ""
    que = deque()
    for i in range(1, n+1):
        if not in_degree[i]:
            que.append(i)
    while que:
        cur = que.popleft()
        answer += str(cur) + " "
        for to_node in graph[cur]:
            in_degree[to_node] -= 1
            if not in_degree[to_node]:
                que.append(to_node)
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N + 1)
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        graph[A].append(B)
        in_degree[B] += 1
    print(solution(N))
