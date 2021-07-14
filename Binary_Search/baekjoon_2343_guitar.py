import sys


def get_m(target):
    _sum, _cnt = 0, 1
    for i in range(len(lessons)):
        if lessons[i] > target:
            _cnt = INF
            break
        if _sum + lessons[i] > target:
            _cnt += 1
            _sum = lessons[i]
        else:
            _sum += lessons[i]
    return _cnt


def solution(start, end, m):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if get_m(mid) > m:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    INF = int(1e9)
    lessons = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(0, INF, M))
