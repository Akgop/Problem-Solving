import sys
N = int(input())

li = [[0]*2 for _ in range(N)]
for i in range(N):
    li[i][0], li[i][1] = map(int, sys.stdin.readline().split())
li.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(li[i][0], li[i][1])
