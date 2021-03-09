def remove_star(li, n, r, c):
    for i in range((n + c), (2*n + c)):
        for j in range((n + r), (2*n + r)):
            li[i][j] = " "


def star_recur(li, n, row, col):
    if n < 3:
        return

    remove_star(li, n // 3, row, col)
    star_recur(li, n // 3, row, col)        # 좌상단
    star_recur(li, n // 3, row + n // 3, col)   # 상단
    star_recur(li, n // 3, row + 2 * (n // 3), col)     # 우상단
    star_recur(li, n // 3, row, col + n // 3)           # 좌측
    star_recur(li, n // 3, row + 2 * (n // 3), col + n // 3)    # 우측
    star_recur(li, n // 3, row, col + 2 * (n // 3))     # 좌하단
    star_recur(li, n // 3, row + (n // 3), col + 2 * (n // 3))     # 하단
    star_recur(li, n // 3, row + 2 * (n // 3), col + 2 * (n // 3))     # 우하단
    return


N = int(input())
star_list = [['*' for i in range(N)] for j in range(N)]
star_recur(star_list, N, 0, 0)
for i in range(N):
    for j in range(N):
        print(star_list[i][j], end="")
    print()
