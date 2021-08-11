from itertools import permutations


def recursion(expression, ops, depth):
    tmp_lst = expression.split(ops[depth])
    # 초기 값 설정
    try:
        answer = int(tmp_lst[0])
    except:
        answer = recursion(tmp_lst[0], ops, depth+1)
    # 계산
    for i in range(1, len(tmp_lst)):
        try:
            value = int(tmp_lst[i])
        except:
            value = recursion(tmp_lst[i], ops, depth+1)
        if ops[depth] == "*":
            answer *= value
        elif ops[depth] == "-":
            answer -= value
        elif ops[depth] == "+":
            answer += value
    return answer


def solution(expression):
    operators = ['*', '-', '+']
    priority = list(permutations(operators, 3))
    answer = 0
    for op in priority:
        answer = max(answer, abs(recursion(expression, op, 0)))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
