import sys


def solution(heights, n, m):
    start = 0
    end = max(heights)      # 처음, 끝 구함
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        # heights 순회하며 탐색
        total = 0
        for height in heights:
            tmp = height - mid
            if tmp > 0:
                total += tmp

        # 총합이 더 크다면
        if total > m:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    Heights = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(Heights, N, M))
