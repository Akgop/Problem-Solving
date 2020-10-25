def count_change(li, cs, cd, rs, rd):
    change_cnt = 0
    for i in range(cs, cd):
        for j in range(rs, rd):
            if (i + j) % 2 == 0:
                if li[i][j] == "W":
                    change_cnt += 1
            elif (i + j) % 2 != 0:
                if li[i][j] == "B":
                    change_cnt += 1
    change_cnt2 = 0
    for i in range(cs, cd):
        for j in range(rs, rd):
            if (i + j) % 2 == 0:
                if li[i][j] == "B":
                    change_cnt2 += 1
            elif (i + j) % 2 != 0:
                if li[i][j] == "W":
                    change_cnt2 += 1
    return min(change_cnt, change_cnt2)


N, M = map(int, input().split())

board = []
for _ in range(N):
    m = list(input())
    board.append(m)

result = N*M
for col in range(N-7):
    for row in range(M-7):
        temp = count_change(board, col, col+8, row, row+8)
        if temp < result:
            result = temp
print(result)
