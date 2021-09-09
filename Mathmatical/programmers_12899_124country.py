def convert_to_123(string):
    result = list(string)
    for i in range(len(result)-1):
        if result[i+1] == '0':
            result[i] = str(int(result[i]) - 1)
            result[i+1] = '3'
    return ''.join(result).lstrip('0')


def zero_exist(string):
    for s in string:
        if s == '0':
            return True
    return False


def convert_3_to_4(string):
    return string.replace('3', '4')


def solution(n):
    exponential = 18
    answer = ''

    e = exponential
    while n < 3 ** e:
        e -= 1

    for i in range(e, -1, -1):
        answer += str(n // (3 ** i))
        n %= 3 ** i

    result = answer
    while zero_exist(result):
        result = convert_to_123(result)
    return convert_3_to_4(result)


print(solution(3))
