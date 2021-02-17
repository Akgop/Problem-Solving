import sys


def solution(sensors, n, k):
    answer = 0
    sensors.sort()
    dist = list()
    for i in range(1, n):
        dist.append(sensors[i] - sensors[i - 1])
    dist.sort()
    answer = sum(dist[0:n-k])
    return answer


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())
    _sensors = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(_sensors, N, K))