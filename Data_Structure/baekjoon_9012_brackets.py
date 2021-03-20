import sys


def solution():
    stack = []
    flag = True
    for e in li:
        if e == ')':
            try:
                stack.pop()
            except:
                flag = False
                break
        if e == '(':
            stack.append(e)
    if stack:
        flag = False
    if flag:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        li = list(sys.stdin.readline().rstrip())
        solution()
