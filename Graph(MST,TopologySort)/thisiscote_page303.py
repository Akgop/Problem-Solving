import sys, copy
from collections import deque


def topology_sort(n):
    result = copy.deepcopy(time)        # 결과를 담을 리스트
    q = deque()

    for idx in range(1, n + 1):
        if indegree[idx] == 0:
            q.append(idx)

    while q:
        now = q.popleft()
        for idx in graph[now]:
            result[idx] = max(result[idx], result[now] + time[idx])
            indegree[idx] -= 1
            if indegree[idx] == 0:
                q.append(idx)
    for idx in range(1, n + 1):
        print(result[idx])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    time = [0] * (N + 1)
    for i in range(1, N + 1):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        time[i] = tmp[0]
        for x in tmp[1:-1]:
            indegree[i] += 1    # 진입차수 카운트
            graph[x].append(i)  # 연결된 edge 정보 저장

    topology_sort(N)
