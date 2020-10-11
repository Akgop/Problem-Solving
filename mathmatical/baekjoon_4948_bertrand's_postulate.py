# 1D Memory Usage
while True:
    n = int(input())
    if n == 0:
        break
    flag = [True] * (n*2+1)
    num = (2*n)
    for i in range(2, int(num**0.5) + 1):
        if flag[i] is True:
            for j in range(2*i, num+1, i):
                flag[j] = False
    cnt = 0
    for i in range(n+1, 2*n+1):
        if flag[i] is True:
            cnt += 1
    print(cnt)

# 반복되는 값을 구할 때 DP 활용한 메모리 적극적으로 활용하기
