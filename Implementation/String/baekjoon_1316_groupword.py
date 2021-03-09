# My Code
n = int(input())
result = 0
for i in range(n):
    cnt = 1
    word = input()
    list_word = list(word)
    set_word = set(word)
    for j in range(len(word)-1):
        if list_word[j] != list_word[j+1]:
            cnt += 1
    if len(set_word) == cnt:
        result += 1
print(result)

# Awesome Code
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# sorted(<str>, key=<str>.find)
# 이렇게 쓰면 순서가 유지된 채로 같은 문자끼리 모아짐
# sorted 와 key, find 에 대해 공부 더 할 것
