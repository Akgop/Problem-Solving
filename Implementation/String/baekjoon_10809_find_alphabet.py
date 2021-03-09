# My Code: Used list comprehension & ASCII converter
arr = list(input())
ascii_arr = [ord(arr[i]) for i in range(len(arr))]
alphabet = [-1 for i in range(26)]
for i in range(len(arr)):
    if alphabet[int(ascii_arr[i])-97] == -1:
        alphabet[int(ascii_arr[i])-97] = i
for i in range(len(alphabet)):
    print(alphabet[i], end=' ')

# Used .find method
# find method -> found: return it's index
# not found: return -1
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end=' ')