# API simulation
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Імітація API
def fetch_data(x):
    time.sleep(1)
    return x

# Послідовне виконання
def sequential_fetch(data):
    start = time.time()
    results = [fetch_data(x) for x in data]
    end = time.time()
    print(f"Sequential: {results}, time: {end - start:.2f}s")
    return results

# Паралельне виконання
def parallel_fetch(data, max_workers=5):
    start = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_data, x) for x in data]
        for f in as_completed(futures):
            results.append(f.result())
    end = time.time()
    print(f"Parallel: {results}, time: {end - start:.2f}s")
    return results

# Використання
if __name__ == "__main__":
    data = list(range(10))

    sequential_fetch(data)
    parallel_fetch(data)