# Using Math Lib
import math
a, b, v = map(int, input().split())
if v == a:
    print(1)
else:
    result = math.ceil((v-a)/(a-b))
    if result == 0:
        result = 1
    print(result+1)

# Without Math Lib
if v == a:
    print(1)
else:
    result = (v-a)//(a-b)
    if (v-a) % (a-b) != 0:
        result += 1
    if result == 0:
        result = 1
    print(result+1)

# Timeout Code
if v == a:
    print(a)
else:
    result = 0
    height = 0
    while True:
        if height >= v-a:
            break
        height += (a-b)
        result += 1
    print(result+1)
