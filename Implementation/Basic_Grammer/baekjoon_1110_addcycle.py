N = int(input())
origin = N
cycle = 0
while True:
    N = (N % 10)*10 + (N//10 + N % 10) % 10
    cycle += 1
    if origin == N:
        break
print(cycle)
