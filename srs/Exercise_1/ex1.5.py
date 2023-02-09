import timeit
import matplotlib.pyplot as plt

def func_cache(n,cache):
    if n == 0 or n == 1:
        return n
    
    if (n in cache):
        return cache[n]
    
    else:
        cache[n] = func_cache(n-1,cache) + func_cache(n-2,cache)
        return cache[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


cache_list = {}

original_times = []
cache_times = []
x_range = []

for n in range(35):
    time = timeit.timeit(lambda: func(n), number=1)
    original_times.append(time)
    print(f"finished {n}th value")
    x_range.append(n)

for n in range(35):
    time = timeit.timeit(lambda: func_cache(n,cache_list),number=1)
    cache_times.append(time)
    print(f"finished {n}th value")


#plt.scatter(x_range,original_times)
plt.scatter(x_range,cache_times)
plt.xlabel("nth number in sequence")
plt.ylabel("time (seconds)")
plt.yscale("linear")
plt.show()