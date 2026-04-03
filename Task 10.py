# Safe execution
from concurrent.futures import ProcessPoolExecutor, as_completed

# Небезпечна функція
def risky(x):
    if x == 0:
        raise ValueError("Division by zero")
    return 10 / x

# Safe wrapper
def safe_execute(func, x):
    try:
        return {"ok": True, "value": func(x)}
    except Exception as e:
        return {"ok": False, "error": str(e), "input": x}

# Safe parallel map
def safe_parallel_map(func, data, max_workers=None):
    results = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(safe_execute, func, x) for x in data]

        for future in as_completed(futures):
            results.append(future.result())

    return results

# Використання
if __name__ == "__main__":
    data = [5, 2, 0, 1, 0]

    results = safe_parallel_map(risky, data)

    for r in results:
        if r["ok"]:
            print(f"Success: {r['value']}")
        else:
            print(f"Error for input {r['input']}: {r['error']}")