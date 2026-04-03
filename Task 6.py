# Порівняння часу
import time
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x * x

data = range(1_000_000)

start = time.time()
result1 = list(map(square, data))
end = time.time()

print("Sequential map time:", end - start)

def parallel_map(func, data):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(func, data))

start = time.time()
result2 = parallel_map(square, data)
end = time.time()

print("Parallel map time:", end - start)