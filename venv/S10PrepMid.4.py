a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(range(0, 20))
print(b)
print(b[::2])
c = list(range(20,0,-2))
print(c)
print(b[-2::-2])
a = list(range(20))
print(a, a[5:])
print(a, a[:6])

for num in a:
    print(num)