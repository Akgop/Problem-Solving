import sys


def solution(n, k):
    result = [0] * n
    result[0] = k[0]
    result[1] = max(k[0], k[1])
    for i in range(2, n):
        # 지금 털 것인지, 안 털고 이전 것을 그대로 사용할 것인지
        # 아래와 같이 작성하는 방법에 익숙해지자
        result[i] = max(result[i-2] + k[i], result[i-1])
    return result[n-1]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    K = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(N, K))
