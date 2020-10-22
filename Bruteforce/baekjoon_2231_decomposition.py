# My Code
N = int(input())

digit = []
result = 0
M = N
while M > 0:
    temp = M
    digit.clear()
    for _ in range(len(str(temp))):
        R = temp % 10
        digit.append(R)
        temp = temp // 10
    if (sum(digit) + M) == N:
        result = M
    M -= 1
print(result)

# Shortest Code
N = int(input())

for i in range(max(1, N-54), N+1):
    if N == i + sum(list(map(int, str(i)))):
        print(i)
        exit(0)
print(0)