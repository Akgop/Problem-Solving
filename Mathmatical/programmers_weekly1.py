def solution(price, money, count):
    answer = ((count * (count + 1)) // 2) * price
    return 0 if money >= answer else (answer - money)


print(solution(3, 20, 4))
