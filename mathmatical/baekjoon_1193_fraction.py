x = int(input())
n = 1
sum_n = 0
while True:
    if n*(n+1) >= 2*x:
        sum_n = n * (n - 1) // 2
        n += 1
        break
    n += 1
a = 0 + (x-sum_n)
b = n - (x-sum_n)
if n % 2 == 0:
    print('%d/%d' % (b, a))
else:
    print('%d/%d' % (a, b))
