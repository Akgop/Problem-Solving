import sys


def print_top_horizontal(idx):
    for i in range(s):
        canvas[0][idx + 1 + i] = '-'


def print_mid_horizontal(idx):
    for i in range(s):
        canvas[(2 * s + 3) // 2][idx + 1 + i] = '-'


def print_bottom_horizontal(idx):
    for i in range(s):
        canvas[2 * s + 3 - 1][idx + 1 + i] = '-'


def print_right_up(idx):
    for i in range(s):
        canvas[i + 1][idx + s + 1] = '|'


def print_right_down(idx):
    for i in range(s):
        canvas[i + 1 + (2 * s + 3) // 2][idx + s + 1] = '|'


def print_left_up(idx):
    for i in range(s):
        canvas[i + 1][idx] = '|'


def print_left_down(idx):
    for i in range(s):
        canvas[i + 1 + (2 * s + 3) // 2][idx] = '|'


li = list(map(int, sys.stdin.readline().rstrip().split()))
s = li[0]
n = str(li[1])
canvas = [[' ']*((s+3)*len(n)) for _ in range(2*s+3)]
for i in range(len(n)):
    index = (s+2)*i+i
    if n[i] == '1':
        print_right_up(index)
        print_right_down(index)
    elif n[i] == '2':
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
        print_right_up(index)
        print_left_down(index)
    elif n[i] == '3':
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
        print_right_up(index)
        print_right_down(index)
    elif n[i] == '4':
        print_mid_horizontal(index)
        print_left_up(index)
        print_right_up(index)
        print_right_down(index)
    elif n[i] == '5':
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
        print_left_up(index)
        print_right_down(index)
    elif n[i] == '6':
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
        print_left_up(index)
        print_left_down(index)
        print_right_down(index)
    elif n[i] == '7':
        print_top_horizontal(index)
        print_right_up(index)
        print_right_down(index)
    elif n[i] == '8':
        print_right_up(index)
        print_right_down(index)
        print_left_up(index)
        print_left_down(index)
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
    elif n[i] == '9':
        print_right_up(index)
        print_right_down(index)
        print_left_up(index)
        print_top_horizontal(index)
        print_mid_horizontal(index)
        print_bottom_horizontal(index)
    else:
        print_right_up(index)
        print_right_down(index)
        print_left_up(index)
        print_left_down(index)
        print_top_horizontal(index)
        print_bottom_horizontal(index)

for i in range(2*s + 3):
    print(''.join(canvas[i]))
