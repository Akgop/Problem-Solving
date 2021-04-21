# import sys
#
#
# def is_ugly(num, ugly_nums):
#     ugly = [2, 3, 5]
#     for u in ugly:
#         while num % u == 0:
#             if (num // u) in ugly_nums:
#                 return True
#             num //= u
#     return False
#
#
# def dp(n):
#     if n <= 5:
#         return n
#     ugly_nums = {1, 2, 3, 4, 5}
#     num = 5
#     answer = 0
#     while len(ugly_nums) < n:
#         if is_ugly(num, ugly_nums):
#             ugly_nums.add(num)
#             answer = num
#         num += 1
#     return answer
#
#
# if __name__ == "__main__":
#     N = int(sys.stdin.readline().rstrip())
#     print(dp(N))

# 위에 코드는 시간초과임. -> O(5000만)
# 가장 작은 숫자에 특정 연산을 곱해서 구함.
n = int(input())
ugly = [0]*n
ugly[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

# O(1000) <- 매우 빠름.
for l in range(1, n):
    ugly[l] = min(next2, next3, next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
print(ugly[n-1])
