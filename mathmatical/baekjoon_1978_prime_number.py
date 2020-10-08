# My Code - O(sqrt(n))
n = int(input())
prime = list(map(int, input().split()))

result = 0
for num in prime:
    if num == 1:
        result += 1
    else:
        for cnt in range(2, int(num ** 0.5) + 1):
            if num % cnt == 0:
                result += 1
                break
print(n - result)

# 소수를 구할 때는 결국 반복문을 돌게 된다.
# 하지만 반쪽만 돌면 되므로
# 루트 n만큼 반복하게 되면 시간복잡도가 O(n)이 아닌
# O(루트n)이 될 수 있다.
