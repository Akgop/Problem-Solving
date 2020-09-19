# My Code
n = int(input())
result = 99
if n <= 99:
    result = n
else:
    for i in range(100, n+1):
        str_n = str(i)
        if (int(str_n[0]) - int(str_n[1])) == (int(str_n[1]) - int(str_n[2])):
            result += 1
print(result)

# Shortest
# 세 수의 등차수열 --> 가운데 수의 두 배 == 양 끝 수의 합 을 이용한 아이디어!
print(sum((i//100+i%10)==i//10%10*2 or i<100 for i in range(1,int(input())+1)))
