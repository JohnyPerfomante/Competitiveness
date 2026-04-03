# Functional pipeline API
from concurrent.futures import ProcessPoolExecutor
from functools import reduce

# Pipeline API
def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result

# Паралельний map
def parallel_map(func, max_workers=None):
    def step(data):
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            return list(executor.map(func, data))
    return step

# Lazy filter
def lazy_filter(predicate):
    def step(data):
        return filter(predicate, data)
    return step

# Reduce
def reduce_step(func, initial=0):
    def step(data):
        return reduce(func, data, initial)
    return step

def square(x):
    return x * x

def greater_than_100(x):
    return x > 100

def sum_reduce(acc, x):
    return acc + x

# Використання
if __name__ == "__main__":
    data = range(100)

    result = pipeline(
        data,
        [
            parallel_map(square),          # map
            lazy_filter(greater_than_100), # filter
            reduce_step(sum_reduce, 0)     # reduce
        ]
    )

    print("Final result:", result)