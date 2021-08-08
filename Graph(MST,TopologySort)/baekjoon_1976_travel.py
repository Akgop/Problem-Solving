import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m):
    parent = [0] * (n + 1)
    for i in range(n + 1):
        parent[i] = i
    graph = list()
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    plan = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        for j in range(i, n):
            if graph[i][j] == 1:
                union_parent(parent, i+1, j+1)
    answer = True
    for i in range(1, m):
        if find_parent(parent, plan[i - 1]) != find_parent(parent, plan[i]):
            answer = False
            break

    return answer


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    if solution(N, M) is True:
        print("YES")
    else:
        print("NO")
