# My Code using set while iteration
arr = input().upper()   # 처음부터 대문자로 입력 받음
result_alpha = "?"
cnt = 0
for c in set(arr):
    if arr.count(c) > cnt:  # 더 큰 값이 나오면
        cnt = arr.count(c)
        result_alpha = c    # 최빈값을 해당 알파벳으로 변환
    elif arr.count(c) == cnt:   # 같은 애 등장하면 최빈값을 "?"로 변환
        result_alpha = "?"
print(result_alpha)

# Other's using list with count(max)
n = input()
n = n.upper()
alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
    result.append(n.count(i))
if result.count(max(result)) > 1:   # 최대값의 개수가 1개 초과면 "?"
    print("?")
else:                               # 1개면 알파벳 출력
    print(alpa[result.index(max(result))])
