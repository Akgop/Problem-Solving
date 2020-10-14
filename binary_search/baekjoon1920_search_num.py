# Without Binary Search --> Timeout
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
# for i in range(m):
#     if b[i] in a:
#         print(1)
#     else:
#         print(0)


# With using QuickSort & Binary Search
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
target = list(map(int, input().split()))
for i in range(m):
    begin = 0
    end = len(a)-1
    result = 0
    while begin <= end:
        mid = (begin + end) // 2
        if target[i] == a[mid]:
            result = 1
            break
        elif target[i] > a[mid]:
            begin = mid + 1
        elif target[i] < a[mid]:
            end = mid - 1
    print(result)

