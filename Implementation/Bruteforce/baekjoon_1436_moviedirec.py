N = int(input())

fix = '666'
answer = 666
while N > 0:
    if fix in str(answer):
        N = N - 1
    answer = answer + 1
print(answer-1)

# Time Complexity : O(n)
# *in* method Time Complexity : O(n)
