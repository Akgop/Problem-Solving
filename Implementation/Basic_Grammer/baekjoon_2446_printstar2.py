# My Code
n = int(input())
for i in range(n):
    print(' '*i, end='')
    print('*'*(2*(n-i)-1))
for i in range(n-1):
    print(' '*(n-i-2), end='')
    print('*'*(2*(i+1)+1))

# Others code 1, range, abs syntax
num = int(input())
for n in range(-num+1, num):
    print(' '*(num-abs(n)-1) + '*'*(2*abs(n)+1))

# Others code 2, print(+) syntax
n=int(input())
for i in range(n):
    print(" "*i + "*"*(2*n-2*i-1))
for j in range(n-1):
    print(" "*(n-j-2) + "*"*(2*j+3))