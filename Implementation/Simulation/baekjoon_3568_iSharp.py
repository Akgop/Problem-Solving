import sys


def is_alphabet(c):
    if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
        return True
    return False


def print_alphabet(li, idx):
    print(' ', end='')
    print(li[:idx-1:-1], end='')
    print(';')


def is_bracket(c):
    if c == ']':
        return True
    return False


def print_bracket(li, idx):
    print(li[idx+1:idx-1:-1], end='')
    return idx+2


if __name__ == '__main__':
    # 문자열 받고
    declaration = sys.stdin.readline().rstrip().split(' ')
    var_type = declaration[0]  # 변수 타입이랑
    values = declaration[1:]   # 변수로 쪼갬

    # 변수 개수만큼 반복 O(N)
    for value in values:
        print(var_type, end='')   # 변수 타입 처음에 출력
        value_r = value[::-1]     # 변수를 reverse
        i = 1                     # ,와 ;를 제거
        while True:
            # 알파벳이라면
            if is_alphabet(value_r[i]):
                print_alphabet(value_r, i)
                break
            # 배열이라면
            if is_bracket(value_r[i]):
                i = print_bracket(value_r, i)
            # 참조나 포인터라면
            else:
                print(value_r[i], end='')
                i += 1
