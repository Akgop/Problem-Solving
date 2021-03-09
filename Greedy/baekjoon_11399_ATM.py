import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
# Greedy 를 사용할 수 있는 정당성 -> 중간에 끼어들기 불가능
P.sort()        # 따라서 오름차순으로 정렬
answer = 0
tmp = 0
for i in range(N):
    tmp += P[i]
    answer += tmp
print(answer)
