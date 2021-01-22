import sys
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        vtx = queue.popleft()
        for v in linked_list[vtx]:
            # 이미 방문한 노드
            if visited[v] is True:
                continue
            # 방문 안한 노드
            queue.append(v)
            visited[v] = True


com = int(sys.stdin.readline().rstrip())
edge_cnt = int(sys.stdin.readline().rstrip())

# 인덱스가 1부터라 +1
linked_list = [[] for _ in range(com+1)]
for _ in range(edge_cnt):
    sv, ev = map(int, sys.stdin.readline().rstrip().split())
    # 단방향이 아니라 양방향 연결을 해주어야 작동한다
    linked_list[sv].append(ev)
    linked_list[ev].append(sv)
visited = [False]*(com+1)
visited[0] = True
bfs(1)
print(visited.count(True) - 2)
