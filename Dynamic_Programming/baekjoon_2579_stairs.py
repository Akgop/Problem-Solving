N = int(input())
s = list()
for i in range(N):
    s.append(int(input()))
if N == 1:
    print(s[0])
elif N == 2:
    print(s[0] + s[1])
elif N == 3:
    print(s[0] + s[2])
else:
    t = [0]*N
    t[0] = s[0]
    t[1] = s[0] + s[1]
    t[2] = (s[0] + s[2]) if (s[0] + s[2]) > (s[1] + s[2]) else (s[1] + s[2])
    for i in range(3, N):
        a = t[i-3] + s[i-1]
        b = t[i-2]
        t[i] = (a if a > b else b) + s[i]
    print(t[-1])
