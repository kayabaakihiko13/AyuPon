from math import sqrt, pow,sin

def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

def prime(n):
    count = 0
    
    if n >= 1000:
        n = 1000
    if n <= 1:
        return -1
    for i in range(2, 1000000):
        if count == n:
            return i - 1
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return -1

def __innerfunction(r, x):
    equation = pow(r, 2) - pow(x, 2)
    return sqrt(equation)

def areaCircle(r):
    return 4*(.5*pow(r,2)*(90+(sin(2*90)/2)))
