# My Code using if-else state
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x, y = 0, 0
if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
else:
    x = x1
if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
else:
    y = y1
print(x, y)

# Other's Code using bit-operator xor
x = y = 0
x ^= x1; y ^= y1
x ^= x2; y ^= y2
x ^= x3; y ^= y3
print(x, y)
