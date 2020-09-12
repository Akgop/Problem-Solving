results = [0, 0, 0, 0, 0]

for i in range(5):
    results[i] = int(input())
    if results[i] < 40:
        results[i] = 40

avg = int(sum(results) / 5)
print(avg)
