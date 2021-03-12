import sys


# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parent = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # union_parent(parent, a, b)
    # kinds = set(parent)
    # return len(kinds)
    return n - 1


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        print(solution())

