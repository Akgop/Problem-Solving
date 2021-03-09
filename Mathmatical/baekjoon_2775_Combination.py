t = int(input())
for i in range(t):
    k = int(input())    # 층
    n = int(input())    # 호
    numerator = k + n
    denominator = min(n-1, k+1)
    result = 1
    # numerator C denominator --> Combination
    if n == 0:
        print(result)
    else:
        for j in range(denominator):
            result *= numerator
            numerator -= 1
        for j in range(denominator):
            result //= denominator
            denominator -= 1
        print(result)
