def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if mem[20][20][20] == -1:
            mem[20][20][20] = w(20, 20, 20)
        return mem[20][20][20]

    if a < b < c:
        if mem[a][b][c-1] == -1:
            mem[a][b][c-1] = w(a, b, c-1)
        if mem[a][b-1][c-1] == -1:
            mem[a][b-1][c-1] = w(a, b-1, c-1)
        if mem[a][b-1][c] == -1:
            mem[a][b-1][c] = w(a, b-1, c)
        return mem[a][b][c-1] + mem[a][b-1][c-1] - mem[a][b-1][c]

    if mem[a-1][b][c] == -1:
        mem[a-1][b][c] = w(a-1, b, c)
    if mem[a-1][b-1][c] == -1:
        mem[a-1][b-1][c] = w(a-1, b-1, c)
    if mem[a-1][b][c-1] == -1:
        mem[a-1][b][c-1] = w(a-1, b, c-1)
    if mem[a-1][b-1][c-1] == -1:
        mem[a-1][b-1][c-1] = w(a-1, b-1, c-1)
    return mem[a-1][b][c] + mem[a-1][b-1][c] + mem[a-1][b][c-1] - mem[a-1][b-1][c-1]


mem = [[[-1]*21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
