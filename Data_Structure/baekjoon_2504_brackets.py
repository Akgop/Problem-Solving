import sys


def recursion(idx, prev):
    count = 0
    flag = True
    while idx < len(string):
        if string[idx] == ")":
            if prev == "(":
                if count == 0:
                    count = 1
                return 2*count, idx+1
            else:
                flag = False
                break
        if string[idx] == "]":
            if prev == "[":
                if count == 0:
                    count = 1
                return 3*count, idx+1
            else:
                flag = False
                break
        if string[idx] == "(" or string[idx] == "[":
            inner, idx = recursion(idx+1, string[idx])
            count += inner
    if flag and prev == "":
        print(count)
    else:
        print(0)
    exit(0)


if __name__ == "__main__":
    string = list(sys.stdin.readline().rstrip())
    _, _ = recursion(0, "")
