equation = input().split('-')
tmp = equation[0].split('+')
answer = 0
for e in tmp:
    answer += int(e)
for e in equation[1:]:  # - 부터는 전부 빼기
    tmp = map(int, e.split('+')) # int 로 형변환
    answer -= sum(tmp)
print(answer)

