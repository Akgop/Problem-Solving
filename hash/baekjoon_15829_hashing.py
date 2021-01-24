L = int(input())
string = input()

answer = 0
for i in range(L):
    tmp = (ord(string[i]) - 96)
    for _ in range(i):
        tmp *= 31
        tmp %= 1234567891
    answer += tmp
print(answer % 1234567891)
