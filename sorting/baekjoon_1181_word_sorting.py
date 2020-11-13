import sys

N = int(input())

li = [""] * N
for i in range(N):
    li[i] = input()

li.sort(key=lambda x: (len(x), x))
print(li[0])
for i in range(1, N):
    if li[i] != li[i-1]:
        print(li[i])


# Set 을 이용하여 중복을 제거하는 방법 <- 다른 사람 코드
word = set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word = list(word)
word.sort()
word.sort(key=lambda x: len(x))
print("\n".join(word))
