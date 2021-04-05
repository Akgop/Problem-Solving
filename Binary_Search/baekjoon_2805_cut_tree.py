import sys


def get_sum(mid):
    result = 0
    for t in trees:
        if t - mid > 0:
            result += t - mid
    return result


def binary_search(start, end, m):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = get_sum(mid)

        if tmp >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    trees = list(map(int, sys.stdin.readline().rstrip().split()))
    print(binary_search(0, 2000000000, M))
