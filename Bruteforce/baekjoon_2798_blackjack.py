N, M = map(int, input().split())
deck = list(map(int, input().split()))
result = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if i == j or i == k or j == k:
                continue
            result.append(deck[i] + deck[j] + deck[k])
result.sort()
maximum = 0
for m in result:
    if m > M:
        break
    maximum = m
print(maximum)
