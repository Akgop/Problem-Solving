import sys


def solution(n):
    for i in range(n-1):
        for j in range(10):
            table[j] = sum(table[j:10]) % 10007
    return sum(table) % 10007


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    table = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(solution(N))
