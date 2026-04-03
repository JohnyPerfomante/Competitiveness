# Паралельна обробка без стану
from concurrent.futures import ThreadPoolExecutor

data = [1, 2, 3, 4, 5]

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    result = list(executor.map(square, data))

print("Result:", result)