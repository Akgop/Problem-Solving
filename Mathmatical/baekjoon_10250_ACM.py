# My Code --> O(1) without input
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    a = n//h    # 호실 번호 - 1
    if n % h == 0:
        b = h
    else:
        b = n - h*a
        a += 1
    print('%d%02d' % (b, a))

# print format %02d -> 정수 2자리수 표기
