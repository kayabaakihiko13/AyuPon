from libc.math cimport sqrt, pow

cpdef int fibonacci(long int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i

    for i in range(n):
        a, b = b, a + b

    return a


cpdef int prime(int n):
    cdef int i, count
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


cpdef double innerfunction(double r, double x):
    cdef double equation = pow(r, 2) - pow(x, 2)
    return sqrt(equation)

cpdef double areaCircle(double r):
    cdef int n = 1000
    cdef double delta_x = (r-0)/n;
    cdef double area_sum = 0.0
    cdef int i
    cdef double x

    for i in range(n):
        x = -r + i * delta_x
        area_sum += innerfunction(r, x) * delta_x
    
    return 4 * area_sum