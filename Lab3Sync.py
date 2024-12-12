import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter
            temp += 1
            counter = temp

def decrement():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter
            temp -= 1
            counter = temp

def run_threads(n, m):
    global counter
    counter = 0
    threads = []

    for _ in range(n):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    for _ in range(m):
        t = threading.Thread(target=decrement)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    with open("Lab8.txt", "w") as file:
        for threads_count in [1, 2, 4, 8]:
            n, m = threads_count, threads_count  # Одинаковое количество инкрементирующих и декрементирующих потоков
            start_time = time.time()
            run_threads(n, m)
            end_time = time.time()
            file.write(f"Число потоков: {n + m}, Итоговое значение счетчика: {counter}, Время выполнения: {end_time - start_time:.4f} секунд\n")

    print(f"Итоговое значение счетчика: {counter}")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")