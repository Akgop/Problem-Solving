import sys


def solution():
    answer = int(li[0])
    for i in range(1, len(li)):
        if answer <= 1 or int(li[i]) <= 1:
            answer += int(li[i])
        else:
            answer *= int(li[i])
    print(answer)


if __name__ == "__main__":
    li = list(sys.stdin.readline().rstrip())
    solution()
