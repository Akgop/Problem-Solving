import sys


def solution(n):
    li.sort(reverse=True)
    count = 0
    i = 0
    while i < len(li):
        i = i + li[i]
        count += 1
    print(count)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N)