import sys


def split_uv(w):
    count = 0
    idx = 0
    correct_u = True
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            correct_u = False
        elif count == 0:
            idx = i+1
            break
    return w[:idx], w[idx:], correct_u


def convert_u(u):
    answer = ''
    for i in range(1, len(u)-1):
        if u[i] == "(":
            answer += ")"
        else:
            answer += "("
    return answer


def dfs(w):
    # 빈 문자열이라면 return
    if not w:
        return ""

    # w를 u와 v로 나눔
    u, v, u_flag = split_uv(w)

    if u_flag:
        return u + dfs(v)
    return "(" + dfs(v) + ")" + convert_u(u)


def solution(p):
    sys.setrecursionlimit(10000)
    answer = dfs(p)
    return answer


print(solution(
    "(()())()"
))

print(solution(
    ")("
))

print(solution(
    "()))((()"
))

print(solution(
    ")))()((("
))