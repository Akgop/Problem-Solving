import sys

# M <= 10000 일 경우 가능한 풀이 Greedy
N, M, K = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort(reverse=True)
answer = 0
while M > 0:
    for j in range(K):
        answer += li[0]  # 가장 큰 수
        M -= 1
    answer += li[1]      # 두 번째로 큰 수
    M -= 1
print(answer)

# M 이 100억 이상 커진다면? 시간초과판정 때문에 Greedy 불가능
# 수학적으로 접근해야함
N, M, K = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort(reverse=True)
q = M // (K+1)         # 전체 수열이 반복되는 횟수
r = M % (K+1)          # 나머지 가장 큰 수만 더해지는 횟수
answer = q * (li[0] * K + li[1]) + r * (li[0])
print(answer)
