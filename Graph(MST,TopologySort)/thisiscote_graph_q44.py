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


def solution(n, planets):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    x = []
    y = []
    z = []
    for i in range(len(planets)):
        x.append((planets[i][0], i))
        y.append((planets[i][1], i))
        z.append((planets[i][2], i))

    x.sort()
    y.sort()
    z.sort()

    edges = []
    for i in range(1, n):
        edges.append([x[i][0] - x[i - 1][0], x[i][1], x[i - 1][1]])
        edges.append([y[i][0] - y[i - 1][0], y[i][1], y[i - 1][1]])
        edges.append([z[i][0] - z[i - 1][0], z[i][1], z[i - 1][1]])

    edges.sort()

    result = 0
    for edge in edges:
        cost, a, b = edge
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            result += cost
    return result


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Planets = []
    for i in range(N):
        Planets.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, Planets))

#
# print(solution(
#     5,
#     [[11, -15, -15],
#      [14, -5, -15],
#      [-1, -1, -5],
#      [10, -4, -1],
#      [19, -4, 19]]
# ))