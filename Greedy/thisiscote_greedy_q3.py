import sys


def solution(n):
    count_up = 0
    count_down = 0
    prev = li[0]
    for i in range(1, n):
        if li[i] != prev:
            if li[i] == '1':
                count_up += 1
            if li[i] == '0':
                count_down += 1
            prev = li[i]
    if li[0] == li[n-1]:
        print(min(count_up, count_down))
    else:
        print(max(count_up, count_down))


if __name__ == "__main__":
    li = list(sys.stdin.readline().rstrip())
    solution(len(li))
