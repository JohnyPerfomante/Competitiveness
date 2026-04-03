# Обробка транзакцій
from concurrent.futures import ProcessPoolExecutor
import math

# Бізнес-логіка
def process_chunk(chunk):
    total = 0
    for x in chunk:
        # filter
        if x % 2 == 0:
            # map
            total += x * x
    return total

def chunked(iterable, chunk_size):
    chunk = []
    for x in iterable:
        chunk.append(x)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

# Паралельний pipeline
def parallel_pipeline(data, chunk_size=10_000, max_workers=None):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        partial_results = executor.map(process_chunk, chunked(data, chunk_size))
        return sum(partial_results)

# Використання
if __name__ == "__main__":
    transactions = range(1_000_000)

    result = parallel_pipeline(transactions)

    print("Final result:", result)