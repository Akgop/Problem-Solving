# Sum of Sequence
n = int(input())
i = 1
if n == 1:
    print(i)
else:
    while True:
        if n <= 3*i*i + 3*i + 1:
            break
        i += 1
    print(i+1)
