import sys


def solution(x):
    table = [0] * (x+1)
    table[2] = 1
    for i in range(3, x+1):
        table[i] = table[i-1] + 1
        if i % 5 == 0:
            table[i] = min(table[i], table[i//5] + 1)
        if i % 3 == 0:
            table[i] = min(table[i], table[i//3] + 1)
        if i % 2 == 0:
            table[i] = min(table[i], table[i//2] + 1)
    return table[x]


if __name__ == "__main__":
    X = int(sys.stdin.readline().rstrip())
    print(solution(X))
