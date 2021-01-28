import sys
from pprint import pprint


R, C, N = map(int, sys.stdin.readline().rstrip().split())

status = []
for _ in range(R):
    status.append(list(sys.stdin.readline().rstrip()))

# 폭탄 여부를 설치된 시간으로 바꿈
for i in range(R):
    for j in range(C):
        if status[i][j] == '.':
            status[i][j] = 0
        else:
            status[i][j] = 1

for it in range(1, N):
    for i in range(R):
        for j in range(C):
            status[i][j] += 1
    if it % 2 == 0:
        for i in range(R):
            for j in range(C):
                # 만약 3 이상이면 터져야댐
                if status[i][j] >= 3:
                    status[i][j] = 0
                    if i > 0:
                        if status[i-1][j] < 3:
                            status[i-1][j] = 0
                    if j > 0:
                        if status[i][j-1] < 3:
                            status[i][j-1] = 0
                    if i < R-1:
                        if status[i+1][j] < 3:
                            status[i+1][j] = 0
                    if j < C-1:
                        if status[i][j+1] < 3:
                            status[i][j+1] = 0

for i in range(R):
    for j in range(C):
        if status[i][j] == 0:
            status[i][j] = '.'
        else:
            status[i][j] = 'O'

for i in range(R):
    print(''.join(status[i]))
