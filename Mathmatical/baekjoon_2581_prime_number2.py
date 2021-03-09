m = int(input())
n = int(input())

result = 0
min_num = 0
first = 0
for num in range(m, n + 1):
    flag = 0
    if num == 1:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = -1
            break
    if flag == 0:
        if first == 0:
            min_num = num
            first = -1
        result += num

if result == 0:
    print(-1)
else:
    print(result)
    print(min_num)
