# My code without map - C style
n = int(input())
num = int(input())
result = 0
for i in range(n):
    result += num % 10
    num = num // 10
print(result)

# using map - Python style
input()
print(list(map(int, input())))

# map: list 의 element 에 함수를 적용시켜 결과를 반환
# Input of map: (function_to_apply, list)
# Output of map: Iterator = next()함수를 갖는 python 객체
