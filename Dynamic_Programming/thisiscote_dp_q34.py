# Longest Increase Subsequence
# 최장 증가 부분 수열로, O(N^2) 알고리즘을 활용하는
# 다이나믹 프로그래밍 문제
# 이분 탐색을 통해 O(N * logN) 으로 구현할 수도 있다.
import sys


def lis(n):
    result = [1] * n
    for i in range(n):
        for j in range(i):
            # 나보다 특정 앞 번호의 병사가 더 클 경우
            if li[j] > li[i]:
                # 이전 결과보다 지금 앞 번호 + 현재 번호의 결과값이 더 큰 경우
                # max 값을 저장하도록 한다.
                result[i] = max(result[i], result[j] + 1)
    print(n - max(result))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    lis(N)
