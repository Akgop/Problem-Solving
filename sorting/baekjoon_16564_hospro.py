import sys


def get_level(mid):
    result = 0
    for x in X:
        if x > mid:
            continue
        result += mid - x
    return result


def solution(x, k):
    start = 0
    end = max(x)

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total_level = get_level(mid)
        if total_level == k:
            answer = mid
            break
        if total_level < k:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    X = list()
    for _ in range(N):
        X.append(int(sys.stdin.readline().rstrip()))
    print(solution(X, K))
