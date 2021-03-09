def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


n = int(input())
if n == 0:
    print(1)
else:
    result = factorial(n)
    print(result)
