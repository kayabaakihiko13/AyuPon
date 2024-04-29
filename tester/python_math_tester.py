import time
from math_pure import fibonacci, prime, areaCircle  # Ganti 'your_module' dengan nama modul Python murni Anda
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
# Rentang nilai n untuk diuji
n_values = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Uji kecepatan fungsi fibonacci - Python
for n in n_values:
    result, exec_time = measure_execution_time(fibonacci, n)
    print(f"Pure Python Fibonacci({n}), Execution Time: {exec_time:.6f} seconds")

# Uji kecepatan fungsi prime - Python
for n in n_values:
    result, exec_time = measure_execution_time(prime, n)
    print(f"Pure Python Prime({n}), Execution Time: {exec_time:.6f} seconds")

# Rentang nilai r untuk diuji
r_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Uji kecepatan fungsi areaCircle - Python
for r in r_values:
    result, exec_time = measure_execution_time(areaCircle, r)
    print(f"Pure Python AreaCircle({r}), Execution Time: {exec_time:.6f} seconds")
