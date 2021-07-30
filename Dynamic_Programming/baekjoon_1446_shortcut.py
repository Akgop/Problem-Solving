import sys


def dp(d):
    shortcuts.sort(key=lambda x: x[1])
    dist = [INF] * (d+1)
    dist[0] = 0
    idx = 0
    for i in range(1, d+1):
        while idx < len(shortcuts) and shortcuts[idx][1] == i:
            dist[i] = min(dist[i], i, dist[shortcuts[idx][0]] + shortcuts[idx][2])
            idx += 1
        dist[i] = min(dist[i], dist[i-1] + 1, i)
    return dist[-1]


if __name__ == "__main__":
    N, D = map(int, sys.stdin.readline().rstrip().split())
    shortcuts = []
    INF = int(1e9)
    for _ in range(N):
        shortcuts.append(list(map(int, sys.stdin.readline().split())))
    print(dp(D))

