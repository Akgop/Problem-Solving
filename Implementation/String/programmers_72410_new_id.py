def convert_to_lower_case(string):
    answer = ''
    for s in string:
        if s.isupper():
            answer += s.lower()
        else:
            answer += s
    return answer


def trim_strange(string):
    answer = ''
    for s in string:
        if s.islower() or s.isdigit() or s == '-' or s == '_' or s == '.':
            answer += s
    return answer


def compress_dot(string):
    answer = ''
    flag = False
    for s in string:
        if s == '.':
            if flag:
                continue
            flag = True
            answer += s
        else:
            if flag:
                flag = False
            answer += s
    return answer


def trim_dot(string):
    return string.strip('.')


def cut_over_15(string):
    if len(string) > 15:
        return string[:15]
    return string


def put_a(string):
    if len(string) == 0:
        return 'a'
    return string


def concat_last(string):
    answer = string
    while len(answer) < 3:
        answer += string[-1]
    return answer


def solution(new_id):
    answer = convert_to_lower_case(new_id)
    answer = trim_strange(answer)
    answer = compress_dot(answer)
    answer = trim_dot(answer)
    answer = put_a(answer)
    answer = cut_over_15(answer)
    answer = trim_dot(answer)
    answer = concat_last(answer)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("=.="))
