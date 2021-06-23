import sys

# 모든 도형 (회전 및 대칭한 모양 포함)
polys = [
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (-1, 0), (-1, 1), (-2, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],

    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (-1, 0), (-1, 1), (-1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (-1, 0), (-2, 0), (-2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],

    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    [(0, 0), (0, 1), (1, 0), (1, 1)],

    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (-1, 1), (0, 1), (1, 1)],
    [(0, 0), (1, -1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
]


def get_max(n, m, poly):
    _max = 0
    for i in range(n):
        for j in range(m):
            _sum = 0
            for coord in poly:
                cx, cy = i + coord[0], j + coord[1]
                # 해당 좌표가 인덱스 범위 넘어가면
                if cx < 0 or cy < 0 or cx >= n or cy >= m:
                    _sum = 0
                    break
                # 안넘어가면
                _sum += graph[cx][cy]
            _max = max(_max, _sum)
    return _max


def solution(n, m):
    result = 0
    for poly in polys:
        result = max(result, get_max(n, m, poly))
    return result


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(N, M))