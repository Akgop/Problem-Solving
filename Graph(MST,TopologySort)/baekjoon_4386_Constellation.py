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



def get_distance(x1, y1, x2, y2):
    return round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)


def solution():
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
            edges.append([dist, points[i][2], points[j][2]])
    edges.sort()

    parent = [i for i in range(len(points))]
    answer = 0
    for dist, a, b in edges:
        if find(a, parent) == find(b, parent):
            continue
        parent = union(a, b, parent)
        answer += dist
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    points = []
    for Idx in range(N):
        A, B = map(float, sys.stdin.readline().rstrip().split())
        points.append([A, B, Idx])
    print(solution())

