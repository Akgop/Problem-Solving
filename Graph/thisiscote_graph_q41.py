# def solution(n, m, spot, plan):
#     print(spot)
#     inf = int(1e9)
#     for i in range(n):
#         for j in range(m):
#             if i == j:
#                 continue
#             if spot[i][j] == 1:
#                 continue
#             spot[i][j] = inf
#
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 spot[i][j] = min(spot[i][j], spot[i][k] + spot[k][j])
#
#     flag = True
#     for i in range(1, m):
#         if spot[plan[i-1] - 1][plan[i] - 1] == inf:
#             flag = False
#             break
#
#     if flag:
#         return "YES"
#     else:
#         return "NO"

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m, spot, plan):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for i in range(n):
        for j in range(i, n):
            if spot[i][j] == 1:
                union(i+1, j+1, parent)

    flag = True
    for i in range(1, len(plan)):
        if parent[plan[i]] != parent[plan[i-1]]:
            flag = False
            break

    if flag:
        return "YES"
    else:
        return "NO"



print(solution(
    5, 4,
    [[0, 1, 0, 1, 1],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 0, 0, 0, 0]],
    [2, 3, 4, 3]
))

print(solution(
    5, 4,
    [[0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [2, 3, 4, 3]
))

print(solution(
    5, 4,
    [[0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [2, 3, 4, 3, 5]
))