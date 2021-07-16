def count(n, d):
    cnt, zero_r = 0, 0
    for i in range(1, n + 1):
        cnt += min(n, (d // i))
        if (d % i) == 0 and (d // i) <= n:
            zero_r += 1
    return cnt, zero_r


def solution(n, k):
    answer = 0
    start, end = 1, min(INF, n**2)
    while start <= end:
        mid = (start + end) // 2
        cnt, zero_r = count(n, mid)
        if zero_r and cnt - zero_r < k <= cnt:
            answer = mid
            break
        if cnt < k:
            start = mid + 1
        else:
            end = mid - 1
    return answer


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    INF = int(1e9)
    print(solution(N, K))