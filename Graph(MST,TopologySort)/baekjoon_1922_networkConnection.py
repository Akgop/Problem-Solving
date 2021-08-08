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


def solution(n, m):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    answer = 0
    for frm, to, cost in edges:
        if find(frm, parent) == find(to, parent):
            continue
        parent = union(frm, to, parent)
        answer += cost
    print(answer)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    edges = []
    for _ in range(M):
        edges.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N, M)