import sys
N = int(input())

count = [0] * 10000

for i in range(N):
    num = int(sys.stdin.readline())
    count[num-1] += 1

for j in range(10000):
    if count[j] != 0:
        for _ in range(count[j]):
            print(j+1)

# 조금이라도 속도를 빠르게 하려면 input() 대신
# sys import 하고 sys.stdin.readline 사용
