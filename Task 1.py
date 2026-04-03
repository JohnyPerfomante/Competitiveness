# Race condition
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter:", counter)

# Результат неправильний, тому що потік змінює змінну counter у циклі: counter += 1. Ця операція не атомарна.

# Race Condition — це ситуація, коли результат програми залежить від порядку виконання потоків, і через це виникають непередбачувані помилки. В даному випадку гонка виникає, бо два потоки одночасно змінюють одну й ту ж змінну.