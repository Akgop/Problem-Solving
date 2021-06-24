import sys


def solution(string):
    flag = 0
    start, end = 0, len(string) - 1
    while end >= start:
        # 앞 뒤가 같으면 pass
        if string[start] == string[end]:
            start, end = start + 1, end - 1
            continue
        # 앞 뒤가 다르면!
        flag += 1
        if string[start + 1] == string[end]:
            start += 1
        elif string[end - 1] == string[start]:
            end -= 1
        else:
            flag = 2
        if flag == 2:
            break
    return flag


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        _str = sys.stdin.readline().rstrip()
        print(solution(_str))
