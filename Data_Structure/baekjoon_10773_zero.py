import sys


def solution(n):
    stack = []
    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
        if num == 0:        # pop 을 보장
            stack.pop()
            continue
        stack.append(num)
    print(sum(stack))


if __name__ == "__main__":
    K = int(sys.stdin.readline().rstrip())
    solution(K)
