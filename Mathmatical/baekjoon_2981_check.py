import sys


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(n):
    numbers.sort()

    answer = numbers[1] - numbers[0]
    for i in range(2, n):
        answer = get_gcd(answer, numbers[i] - numbers[i-1])

    result = set()
    for i in range(2, int(answer**0.5) + 1):
        if answer % i == 0:
            result.add(i)
            result.add(answer//i)

    li = list(result)
    li.sort()

    for i in li:
        print(i, end=' ')
    print(answer)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = list()
    for _ in range(N):
        numbers.append(int(sys.stdin.readline().rstrip()))
    solution(N)