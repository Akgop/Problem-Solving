def dfs(n):
    P[1] = 1
    P[2] = 1
    P[3] = 1
    P[4] = 2
    P[5] = 2
    for i in range(6, n+1):
        P[i] = P[i-5] + P[i-1]
        # also P[i-2] + P[i-3] satisfies


T = int(input())
I = []
for _ in range(T):
    I.append(int(input()))
P = [0] * (max(I)+6)
dfs(max(I))
for e in range(T):
    print(P[I[e]])
