# Паралельний map
from concurrent.futures import ThreadPoolExecutor

def parallel_map_safe(func, data, max_workers=None):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, x) for x in data]
        
        for f in futures:
            try:
                results.append(f.result())
            except Exception as e:
                results.append(f"Error: {e}")
    
    return results