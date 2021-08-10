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


def get_distance(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def solution(n):
    edges = []
    parent = [i for i in range(n+1)]

    for a, b in already:
        union(a, b, parent)

    # 간선 길이 구하기
    for i in range(1, n):
        for j in range(i+1, n+1):
            dist = get_distance(points[i][0], points[j][0], points[i][1], points[j][1])
            edges.append([dist, i, j])

    edges.sort(key=lambda x: x[0])
    answer = 0
    for dist, a, b in edges:
        if find(a, parent) == find(b, parent):
            continue
        union(a, b, parent)
        answer += dist
    print(format(answer, ".2f"))


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    points = [[]]
    already = []
    for idx in range(N):
        points.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for _ in range(M):
        already.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution(N)
