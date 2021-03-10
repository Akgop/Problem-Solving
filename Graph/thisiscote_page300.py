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


def solution():
    edges.sort()
    result = 0
    last = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost
    return result - last


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    edges = list()
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = i
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().rstrip().split())
        edges.append((C, A, B))
    print(solution())
