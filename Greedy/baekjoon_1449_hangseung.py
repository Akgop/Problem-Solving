import sys


def solution(l):
    count = 1
    start = spots.pop()
    while spots:
        now = spots.pop()
        if start+0.5 - (now-0.5) <= l:
            continue
        start = now
        count += 1
    return count


if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    spots = list(map(int, sys.stdin.readline().split()))
    spots.sort()
    print(solution(L))
