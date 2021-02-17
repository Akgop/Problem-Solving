import sys


def solution(a, b):
    answer = -1
    cnt = 1
    while b > a:
        if b % 2 == 0:
            b //= 2
            cnt += 1
        elif b % 10 == 1:
            b -= 1
            b //= 10
            cnt += 1
        else:
            break
    if a == b:
        answer = cnt
    return answer


if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(solution(A, B))
