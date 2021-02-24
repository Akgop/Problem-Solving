import sys


def solution(a, b, k):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] >= b[i]:
            break
        a[i], b[i] = b[i], a[i]
    return sum(a)


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    li_a = (list(map(int, sys.stdin.readline().rstrip().split())))
    li_b = (list(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(li_a, li_b, K))
