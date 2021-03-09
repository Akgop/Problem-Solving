def hanoi(n, fr, to, tmp, mv, c):
    if n == 1:
        mv.append(fr)
        mv.append(to)
        c += 1
        return c

    c = hanoi(n-1, fr, tmp, to, mv, c)
    mv.append(fr)
    mv.append(to)
    c += 1
    c = hanoi(n-1, tmp, to, fr, mv, c)
    return c


N = int(input())
cnt = 0
move = []
cnt = hanoi(N, 1, 3, 2, move, cnt)
print(cnt)
for i in range(0, len(move), 2):
    print(move[i], move[i+1])


