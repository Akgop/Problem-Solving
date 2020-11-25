def cal(n):
    answer = A[0]
    for i in range(n-1):
        if result[i] == 0:
            answer = answer + A[i + 1]
        elif result[i] == 1:
            answer = answer - A[i + 1]
        elif result[i] == 2:
            answer = answer * A[i + 1]
        else:
            if answer < 0:
                answer = 0 - (abs(answer) // A[i + 1])
            else:
                answer = answer // A[i + 1]
    return answer


def dfs(depth, n):
    if depth == n-1:
        ans.append(cal(n))
        return
    for j in range(4):
        if Op[j] != 0:
            Op[j] -= 1
            result.append(j)
            dfs(depth+1, n)
            result.pop()
            Op[j] += 1


N = int(input())
A = list(map(int, input().split()))
Op = list(map(int, input().split()))
result = []
ans = []
dfs(0, N)
print(max(ans), min(ans))

