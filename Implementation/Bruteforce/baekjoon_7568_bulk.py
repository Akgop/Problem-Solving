N = int(input())
x_list = []
y_list = []
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

rank_list = []
rank = 1
key_x, key_y = 0, 0
for (x1, y1) in zip(x_list, y_list):
    rank = 1
    for (x2, y2) in zip(x_list, y_list):
        if x1 < x2 and y1 < y2:
            rank += 1
    print(rank, end=" ")

# zip method: multiple list iteration simultaneously
