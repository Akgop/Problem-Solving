N = int(input())

answer = 0
for i in range(N+1):
    if '3' in str(i):
        answer += 3600
        continue
    for j in range(60):
        if '3' in str(j):
            answer += 60
            continue
        for k in range(60):
            if '3' in str(k):
                answer += 1
print(answer)
