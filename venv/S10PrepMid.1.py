def factorial(num):
    p = 1
    for i in range(1, num+1):
        p *= i
        return p
    # si no pones el rannge, y solo(num), también multiplicara por 0

def rec_fac(num):
    if num == 1:
        return 1
    return num*rec_fac(num-1)


print(rec_fac(7))

