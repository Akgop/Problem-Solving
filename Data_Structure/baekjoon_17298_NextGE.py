import sys


def solution(n):
    result = [-1] * n
    stack = [[li[0], 0]]

    for i in range(1, n):
        while stack:
            if stack[-1][0] < li[i]:
                result[stack[-1][1]] = li[i]
                stack.pop()
            else:
                break
        stack.append([li[i], i])

    for r in result:
        print(r, end=" ")


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(N)