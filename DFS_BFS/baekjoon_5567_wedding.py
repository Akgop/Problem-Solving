import sys
from collections import deque


def bfs(start, visited):
    queue = deque()
    depth = 0
    queue.append((start, depth))
    visited[start] = True

    while queue:
        vtx = queue.popleft()
        depth = vtx[1] + 1
        if depth > 2:
            break
        for v in linked_list[vtx[0]]:
            if visited[v] is True:
                continue
            queue.append((v, depth))
            visited[v] = True

    return visited.count(True) - 2


def solution(ll):
    visited = [False] * (N + 1)
    visited[0] = True
    answer = bfs(1, visited)
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    linked_list = [[] for _ in range(N+1)]
    for _ in range(M):   # 양방향
        se, ee = map(int, sys.stdin.readline().rstrip().split())
        linked_list[se].append(ee)
        linked_list[ee].append(se)
    print(solution(linked_list))

