import sys


def is_palindrome(string, start, end):
    while start <= end:
        if string[start] == string[end]:
            start, end = start + 1, end - 1
            continue
        else:
            return start, end
    return start, end


def is_pseudo(string, start, end):
    start, end = is_palindrome(string, start, end)
    if start > end:
        return 1
    else:
        return 2


def solution(string):
    start, end = is_palindrome(string, 0, len(string) - 1)
    if start > end:     # 팰린드롬인 경우
        return 0
    else:
        result = is_pseudo(string, start + 1, end)
        if result == 2:
            result = is_pseudo(string, start, end - 1)
        return result


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        _str = sys.stdin.readline().rstrip()
        print(solution(_str))
