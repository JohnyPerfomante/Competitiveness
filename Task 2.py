# Усунення проблеми
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Блокування на час інкременту
            counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter with lock:", counter)

# Чому це працює? Lock забезпечує взаємне виключення: тільки один потік може зайти в критичну секцію в конкретний момент часу. Інші потоки, які намагаються взяти lock, чекають, поки він звільниться. Це гарантує, що спільна змінна змінюється атомарно.

# Мінуси підходу: кожен інкремент блокується окремо, що створює затримки, особливо при великій кількості потоків. Якщо програма складніша, можна помилково захопити lock у неправильному порядку.