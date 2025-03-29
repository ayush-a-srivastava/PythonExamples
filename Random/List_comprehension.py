import time

# Traditional loop
start = time.time()
squares_loop = []
for i in range(1_000_000):
    squares_loop.append(i ** 2)
end = time.time()
print("Loop Time:", end - start)

# List comprehension
start = time.time()
squares_comp = [i ** 2 for i in range(1_000_000)]
end = time.time()
print("List Comprehension Time:", end - start)
