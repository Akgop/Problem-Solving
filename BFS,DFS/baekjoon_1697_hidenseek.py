import sys
from collections import deque


def bfs(start, target, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        cur = queue.popleft()
        # 현재 노드가 타겟 노드이면
        if cur == target:
            break
        # 이미 방문한 노드가 아니면 추가
        if cur - 1 >= 0:
            if visited[cur - 1] == -1:
                queue.append(cur-1)
                visited[cur-1] = visited[cur] + 1
        if cur + 1 < 100001:
            if visited[cur + 1] == -1:
                queue.append(cur + 1)
                visited[cur + 1] = visited[cur] + 1
        if cur * 2 < 100001:
            if visited[cur * 2] == -1:
                queue.append(cur*2)
                visited[cur*2] = visited[cur] + 1
    return visited[target]


def solution(n, k):
    visited = [-1] * 100001
    return bfs(n, k, visited)


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(solution(N, K))
