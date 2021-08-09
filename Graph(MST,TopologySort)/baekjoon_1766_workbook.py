import sys
import heapq


def solution(n):
    heap = []
    answer = ""
    for i in range(1, n+1):
        if not in_degree[i]:
            heapq.heappush(heap, i)
    while heap:
        cur_node = heapq.heappop(heap)
        answer += str(cur_node) + " "
        for to_node in connections[cur_node]:
            in_degree[to_node] -= 1
            if not in_degree[to_node]:
                heapq.heappush(heap, to_node)
    print(answer)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    in_degree = [0] * (N + 1)
    connections = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        in_degree[B] += 1
        connections[A].append(B)
    solution(N)
