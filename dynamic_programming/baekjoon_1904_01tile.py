N = int(input())
result = [0] * (N + 1)
result[0] = 1
result[1] = 2
for i in range(2, N):
    result[i] = (result[i-1] + result[i-2]) % 15746
print(result[N - 1])
