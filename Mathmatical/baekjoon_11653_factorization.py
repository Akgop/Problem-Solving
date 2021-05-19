import sys

n = int(sys.stdin.readline().rstrip())
sqrt_n = int(n ** 0.5) + 1

prime = [True] * sqrt_n
prime[0] = False
prime[1] = False
for i in range(2, int(sqrt_n ** 0.5) + 1):
    j = 2
    while i * j < sqrt_n:
        prime[i * j] = False
        j += 1

prime_list = []
for i in range(sqrt_n):
    if prime[i]:
        prime_list.append(i)

idx = 0
result = []
while n > 1:
    if idx == len(prime_list):
        result.append(n)
        break
    if n % prime_list[idx] == 0:
        n //= prime_list[idx]
        result.append(prime_list[idx])
    else:
        idx += 1

for i in range(len(result)):
    print(result[i])


