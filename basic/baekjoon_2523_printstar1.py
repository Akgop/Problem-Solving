# My Algorithm
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*", end='')
    print()

# I studied after.
n = int(input())
for i in range(n):
    print('*'*(i+1))    # print * syntax
for j in range(n-1):
    print('*'*(n-1-j))