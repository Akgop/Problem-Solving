import sys


def solution(numbers, targets, n, m):
    # 이 문제는 set 을 이용하여 hash 자료형을 이용하여 구현할 수 있다.
    # 오히려 이진탐색보다 코드가 간결해져 편하다. 항상 쉽게 풀 수 있는 여러 방법을 생각해보자.
    number_set = set(numbers)    # O(N)
    for target in targets:       # O(M)
        if target in number_set:   # hash 구조라 in method = O(1)
            print("yes", end=' ')
        else:
            print("no", end=' ')


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    Numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    Targets = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(Numbers, Targets, N, M)
