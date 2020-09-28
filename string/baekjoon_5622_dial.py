# My Code
arr = list(input())
num = [(ord(arr[i])-65)//3+3 for i in range(len(arr))]
for i in range(len(arr)):   # error handle when 'S,V'
    if arr[i] == 'S':
        num[i] = 8
    if arr[i] == 'V':
        num[i] = 9
for i in range(len(num)):   # error handle when 'Y,Z'
    if num[i] > 10:
        num[i] = 10
print(sum(num))

# Shortest
print(sum((ord(i)-62-(i in 'SVYZ')-(i=='Z'))//3+2 for i in input()))