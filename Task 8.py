# Паралельний pipeline
from concurrent.futures import ProcessPoolExecutor
from functools import reduce

data = range(100)

# Map
def square(x):
    return x * x

# Filter
def greater_than_100(x):
    return x > 100

# Reduce
def sum_reduce(acc, x):
    return acc + x

# Паралельний pipeline
def parallel_pipeline(data):
    with ProcessPoolExecutor() as executor:
        mapped = list(executor.map(square, data))
    
    filtered = filter(greater_than_100, mapped)
    
    result = reduce(sum_reduce, filtered, 0)
    
    return result


result = parallel_pipeline(data)
print("Result:", result)