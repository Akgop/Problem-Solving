import sys


def get_distance():
    answer = 0
    for h in houses:
        minimum = 200
        for s in selected:
            dist = abs(h[0] - s[0]) + abs(h[1] - s[1])
            if dist < minimum:
                minimum = dist
        answer += minimum
    result.append(answer)


def backtrack(depth, s, e, m):
    if depth == m:
        get_distance()
        return
    for i in range(s, e):
        if not visited[i]:
            visited[i] = True
            selected.append(chickens[i])
            backtrack(depth + 1, i, e, m)
            selected.pop()
            visited[i] = False


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = list()
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    chickens = list()
    houses = list()
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 2:
                chickens.append((x, y))
            if graph[x][y] == 1:
                houses.append((x, y))
    selected = list()
    visited = [False] * len(chickens)
    result = list()
    backtrack(0, 0, len(chickens), M)
    result.sort()
    print(result[0])
