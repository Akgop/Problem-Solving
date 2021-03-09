t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if dist == (r1+r2)**2 or dist == (r1-r2)**2:
        print(1)
    elif (r1-r2)**2 < dist < (r1+r2)**2:
        print(2)
    else:
        print(0)
