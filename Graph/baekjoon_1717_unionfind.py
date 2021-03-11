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
    for _ in range(m):
        cmd, a, b = map(int, sys.stdin.readline().rstrip().split())
        if cmd == 0:
            union_parent(parent, a, b)
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    N, M = map(int, sys.stdin.readline().rstrip().split())
    solution(N, M)
