n = int(input())
result = 0
for i in range(n//3):
    if n % 5 == 0:
        result += n // 5
        n = 0
        break
    n = n - 3
    result += 1
if n != 0:
    result = -1
print(result)
