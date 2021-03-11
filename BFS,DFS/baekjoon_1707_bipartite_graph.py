import sys
from collections import deque

def dfs(v, color):
    # 현재 노드 방문 처리
    visited[v] = 3 - color
    for i in linked_list[v]:
        if visited[i] == visited[v]:
            return False
        if visited[i] == 0:
            if not dfs(i, visited[v]):
                return False
    return True


# def bfs(start, color):
#     q = deque()
#     q.append(start)
#     visited[start] = color
#     while q:
#         cur_i = q.popleft()
#         for nxt in linked_list[cur_i]:
#             # 미방문 -> 방문 처리
#             if visited[nxt] == 0:
#                 visited[nxt] = 3 - visited[cur_i]
#                 q.append(nxt)
#             # 겹침 -> 종료
#             if visited[nxt] == visited[cur_i]:
#                 return False
#     return True


def solution(v, e):
    flag = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not dfs(i, 1):
                flag = False
                break
            # if not bfs(i, 1):
            #     flag = False
            #     break
    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    K = int(sys.stdin.readline().rstrip())
    for _ in range(K):
        V, E = map(int, sys.stdin.readline().rstrip().split())
        linked_list = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)
        for _ in range(E):
            sv, ev = map(int, sys.stdin.readline().rstrip().split())
            linked_list[sv].append(ev)
            linked_list[ev].append(sv)
        solution(V, E)
