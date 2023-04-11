a= []
print(f"a is {a}, type of a={type(a)}")

a = [1, 2, 3, 4]
print(a)
b = [1.2, -9, 10, "bob"]
print (b)
c = [1, 2.3, 0, True, "xxxx", print, None]
print (c)
print(b[1])
c[5](b[1])
print(c[-1])
#len el numero de elemntos
print(len(c))
d = a + b
print(d)
e= 3*a
print(e)
# Es solo una lista
# Aqui es una lista de 4 elementos los cuales son listas
f= [a, a, a, a]
print(f)
print(f, f[2], f[2][2])