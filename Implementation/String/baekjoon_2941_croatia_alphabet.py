# My Code
arr = input()
result = len(arr)
result = result - arr.count('c=') - arr.count('c-') - arr.count('d-')
result = result - arr.count('s=') - arr.count('nj') - arr.count('lj')
result = result - arr.count('dz=') - arr.count('z=')
print(result)

# Shortest Code
w = input(); print(len(w)-sum(w.count(a) for a in['=', '-', 'lj', 'nj', 'dz=']))

# Semi-colon in python
# multiple statements in one line
