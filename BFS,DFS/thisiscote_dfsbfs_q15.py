import sys
from collections import deque


def bfs(start, k):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    answer = list()
    while q:
        node, depth = q.popleft()
        # 종료 조건: 만약 찾는 depth 가 더 깊어졌음
        if depth > k:
            break
        # 만약 내가 원하던 노드임
        elif depth == k:
            answer.append(node)

        # 현재 주변 노드 순회하며 queue 에 추가
        for e in adj_lst[node]:
            # 이미 방문
            if visited[e]:
                continue
            # 아직 방문 x
            q.append((e, depth + 1))
            visited[e] = True
    if not answer:
        print(-1)
        return
    answer.sort()
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[a].append(b)
    visited = [False] * (N+1)
    bfs(X, K)
