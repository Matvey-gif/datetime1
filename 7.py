import time

def slow_function():
    time.sleep(2)

start_time = time.time()
slow_function()
end_time = time.time()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.2f} секунд")