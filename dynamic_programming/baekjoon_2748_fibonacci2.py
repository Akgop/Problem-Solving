n = int(input())
fibonacci = [0]*(n+1)
fibonacci[0] = 0
fibonacci[1] = 1

for i in range(2, n+1):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

print(fibonacci[n])

# 입력 N이 큰 경우 재귀 대신 DP 사용
