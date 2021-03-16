import sys


# A 부터 B 까지 2와 5로 소인수 분해 ( a < b )
def count_num(n, divisor):
    count = 0
    tmp = divisor
    while n >= divisor:
        count += n // divisor
        divisor = divisor * tmp
    return count


def solution(n, m):
    if n < 5:
        return 0
    two = count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)
    five = count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5)

    answer = min(two, five)
    if answer < 0:
        answer = 0
    return answer


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print(solution(N, M))
