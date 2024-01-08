import time

start = time.perf_counter()

a = 0
for i in range(pow(10, 8)):
    a += 1

print(f"Time taken: {time.perf_counter()-start}s")
