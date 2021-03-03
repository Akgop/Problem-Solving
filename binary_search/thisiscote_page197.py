import sys


def binary_search(li, target, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2
    if li[mid] == target:
        return mid
    elif target < li[mid]:
        return binary_search(li, target, start, mid - 1)
    else:
        return binary_search(li, target, mid + 1, end)


# O((M + N) * logN) = O(NlogN)[정렬] + O(M * logN)[이진탐색]
def solution(numbers, targets, n, m):
    # 이진 탐색은 데이터가 정렬된 상태에서 사용
    numbers.sort()           # O(NlogN)
    for target in targets:   # O(M)
        answer = binary_search(numbers, target, 0, n)  # O(M) * O(logN)
        if answer is None:
            print("no", end=' ')
        else:
            print("yes", end=' ')


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    Targets = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(Numbers, Targets, N, M)
