m, n = map(int, input().split())

for num in range(m, n+1):
    if num == 1:
        continue
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag is True:
        print(num)
