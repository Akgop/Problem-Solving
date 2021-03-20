import sys


def solution(s):
    stack = []
    flag = True
    for e in s:
        if e == '(' or e == '[':
            stack.append(e)
        if e == ')':
            try:
                now = stack.pop()
                if now != '(':
                    flag = False
                    break
            except:
                flag = False
                break
        if e == ']':
            try:
                now = stack.pop()
                if now != '[':
                    flag = False
                    break
            except:
                flag = False
                break
    if stack:
        flag = False
    if flag:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    while True:
        string = sys.stdin.readline().rstrip()
        if string == '.':
            break
        solution(string)