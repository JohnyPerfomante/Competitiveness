# Без mutable state
def increment(x):
    return x + 1

data = [0] * 200000

result = list(map(increment, data))

final_sum = sum(result)

print("Final result:", final_sum)