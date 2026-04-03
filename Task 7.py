# CPU-bound задача
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def heavy_task(x):
    total = 0
    for i in range(10_000_000):
        total += i * x
    return total

data = [1, 2, 3, 4]

# 1. Послідовно
start = time.time()
result_seq = [heavy_task(x) for x in data]
end = time.time()
print("Sequential time:", end - start)

# 2. ThreadPool
start = time.time()
with ThreadPoolExecutor() as executor:
    result_thread = list(executor.map(heavy_task, data))
end = time.time()
print("ThreadPool time:", end - start)

# 3. ProcessPool
start = time.time()
with ProcessPoolExecutor() as executor:
    result_process = list(executor.map(heavy_task, data))
end = time.time()
print("ProcessPool time:", end - start)

# ProcessPoolExecutor — найшвидший