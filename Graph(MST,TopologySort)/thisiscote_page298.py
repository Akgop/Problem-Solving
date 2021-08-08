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


def solution(cmd):
    for c in cmd:
        if c[0] == 0:
            union_parent(parent, c[1], c[2])
        else:
            if find_parent(parent, c[1]) == find_parent(parent, c[2]):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    Cmd = list()
    parent = [0] * (N+1)
    for i in range(N+1):
        parent[i] = i
    for _ in range(M):
        func, A, B = map(int, sys.stdin.readline().rstrip().split())
        Cmd.append((func, A, B))
    solution(Cmd)