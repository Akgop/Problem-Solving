import sys
from collections import deque


def solution(n):
    que = deque()
    result = [0] * (n + 1)
    for i in range(1, len(in_degree)):
        if in_degree[i] == 0:
            que.append(i)
            result[i] = build_time[i]
    while que:
        cur = que.popleft()
        for nxt in builds[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                que.append(nxt)
            result[nxt] = max(result[cur] + build_time[nxt], result[nxt])
    return "\n".join(map(str, result[1:]))


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    builds = dict()
    build_time = [0] * (N+1)
    in_degree = [0] * (N+1)
    for idx in range(1, N+1):
        builds[idx] = []
    for idx in range(1, N+1):
        tmp = list(map(int, sys.stdin.readline().split()))[:-1]
        build_time[idx] = tmp[0]
        for idx2 in range(1, len(tmp)):
            builds[tmp[idx2]].append(idx)
        in_degree[idx] += len(tmp[1:])
    print(solution(N))
