# My Code
n = int(input())
for i in range(2*n):
    if i % 2 == 0:  # even
        for j in range(n):
            if j % 2 == 0:
                print('*', end='')
            else:
                print(' ', end='')
    else:   # odd
        for j in range(n):
            if j % 2 == 0:
                print(' ', end='')
            else:
                print('*', end='')
    print('')

# Shortest
n=int(input())
print(('* '*((n+1)//2)+'\n'+' *'*(n//2)+'\n')*n,end='')