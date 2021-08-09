import sys


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent


def solution(n):
    parent = [i for i in range(n)]
    for i in range(len(edges)):
        a, b = edges[i][0], edges[i][1]
        if find(a, parent) == find(b, parent):
            return i + 1
        parent = union(a, b, parent)
    return 0


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    edges = []
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        edges.append([A, B])
    print(solution(N))


