import time
import AyuPon.math  # Modul Cython

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Rentang nilai n untuk diuji
n_values = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Uji kecepatan fungsi fibonacci - Cython
for n in n_values:
    result, exec_time = measure_execution_time(AyuPon.math.fibonacci, n)
    print(f"Fibonacci({n}) - Cython: {result}, Execution Time: {exec_time:.6f} seconds")

# Uji kecepatan fungsi prime - Cython
for n in n_values:
    result, exec_time = measure_execution_time(AyuPon.math.prime, n)
    print(f"Prime({n}) - Cython: {result}, Execution Time: {exec_time:.6f} seconds")

# Rentang nilai r untuk diuji
r_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,1000,10_000]

# Uji kecepatan fungsi areaCircle - Cython
for r in r_values:
    result, exec_time = measure_execution_time(AyuPon.math.areaCircle, r)
    print(f"AreaCircle({r}) - Cython: {result}, Execution Time: {exec_time:.6f} seconds")
