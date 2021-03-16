import sys
import math


# 에라토스테네스의 체
def prime_sieve(sieve_size):
    sieve = [True] * (sieve_size + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(sieve_size**0.5) + 1):
        if sieve[i] is False:
            continue
        for j in range(i**2, sieve_size+1, i):
            sieve[j] = False
    primes = []
    for i in range(sieve_size + 1):
        if sieve[i]:
            primes.append(i)
    return primes


def get_prime_number(n):
    prime_list = prime_sieve(n)
    factors = dict()
    # 소수 리스트 돌면서
    for i in range(2, n + 1):
        for p in prime_list:
            count = 0
            # 나눠지면 나눈다.
            while i % p == 0:
                i /= p
                # 몇번 나누었는지 카운트 하고
                count += 1
            if count > 0:
                try:
                    factors[p] += count
                except:
                    factors[p] = count
    return factors


def solution(n):
    if N < 5:
        print(0)
    else:
        result = get_prime_number(n)
        # print(result[2], result[5])
        print(min(result[2], result[5]))


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    solution(N)
