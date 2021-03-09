# Only for Pypy3
N = int(input())
li = []
for i in range(N):
    li.append(int(input()))
li.sort()
print("\n".join(map(str, li)))
# print("\n".join(map(str, sorted(li))))
# 이렇게 sorted 로 바로 넣어줄 수도 있다.

