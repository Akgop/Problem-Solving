import sys
N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))  # N-1 개
cost = list(map(int, sys.stdin.readline().split()))    # N 개
tmp = cost[0]
answer = 0
for i in range(N-1):
    if cost[i] < tmp:   # 현재 가격이 싸면
        tmp = cost[i]   # 해당 가격으로 업데이트
    answer += (tmp * length[i])
print(answer)
