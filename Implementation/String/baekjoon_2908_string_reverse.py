# My Code - 2 way to reverse string
a, b = input().split(' ')

a = int(''.join(reversed(a)))
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)
