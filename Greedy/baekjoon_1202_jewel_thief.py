import sys


def solution(jewels, c):
    answer = 0
    loaded = [False] * len(c)

    # sort -> O(NlogN)
    jewels.sort(key=lambda x: x[1], reverse=True)  # reverse -> O(N)
    c.sort()  # ascending order

    for jewel in jewels:    # (m, v) -> 30만개
        for i in range(len(c)):   # c = 30만개 -> N^2?
            if jewel[0] <= c[i]:




    return answer


if __name__ == "__name__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    Jewels = list()
    C = list()
    for _ in range(N):
        M, V = map(int, sys.stdin.readline().rstrip().split())
        Jewels.append((M, V))
    for _ in range(K):
        C.append(int(sys.stdin.readline().rstrip()))
    print(solution(Jewels, C))
