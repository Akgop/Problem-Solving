burger = 2000
drink = 2000

for i in range(3):
    temp = int(input())
    if temp < burger:
        burger = temp

for j in range(2):
    temp = int(input())
    if temp < drink:
        drink = temp

result = burger + drink - 50
print(result)
