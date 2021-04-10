import sys


N = int(sys.stdin.readline().rstrip())
li = list()
for _ in range(N):
    name, kor, eng, math = map(str, sys.stdin.readline().rstrip().split())
    li.append((name, int(kor), int(eng), int(math)))

li.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(li[i][0])
