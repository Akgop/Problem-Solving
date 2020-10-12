x, y, w, h = map(int, input().split())

dist1 = x - 0
dist2 = y - 0
dist3 = w - x
dist4 = h - y
print(min(dist1, dist2, dist3, dist4))
