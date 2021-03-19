import sys


def solution(n):
    left = li[0:n//2]
    right = li[n//2:n]
    if sum(left) == sum(right):
        print("LUCKY")
    else:
        print("READY")


if __name__ == "__main__":
    li = list(map(int, sys.stdin.readline().rstrip()))
    solution(len(li))
