import sys


def get_sum(mid):
    answer = 0
    for length in lan:
        answer += length // mid
    return answer


def binary_search(n):
    start = 0
    end = 2**31 - 1

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        count = get_sum(mid)
        # 아직 모자르다면
        if n > count:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer


if __name__ == "__main__":
    K, N = map(int, sys.stdin.readline().rstrip().split())
    lan = list()
    for _ in range(K):
        lan.append(int(sys.stdin.readline().rstrip()))
    print(binary_search(N))
