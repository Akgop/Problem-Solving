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


def solution(n, m, roads):
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    roads.sort(key=lambda x: x[2])

    # 도로 길이 합을 미리 다 구해놓는다.
    total = 0
    for i in range(m):
        total += roads[i][2]

    for x, y, z in roads:
        # 사이클이 형성되지 않을 때, 도로에서 길이를 뺀다(합친다)
        if find(x, parent) != find(y, parent):
            union(x, y, parent)
            total -= z

    return total


print(solution(
    7, 11,
    [[0, 1, 7],
     [0, 3, 5],
     [1, 2, 8],
     [1, 3, 9],
     [1, 4, 7],
     [2, 4, 5],
     [3, 4, 15],
     [3, 5, 6],
     [4, 5, 8],
     [4, 6, 9],
     [5, 6, 11]]
))