import time


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    return wrapper


@memoize
def fibonacci_with_memoize(n):
    if n < 2:
        return n
    return fibonacci_with_memoize(n - 1) + fibonacci_with_memoize(n - 2)


def fibonacci_no_memoize(n):
    if n < 2:
        return n
    return fibonacci_no_memoize(n - 1) + fibonacci_no_memoize(n - 2)


def run_fibonacci_no_memoize():
    start_time = time.time()
    fibonacci_no_memoize(30)
    end_time = time.time()
    print(f"Время выполнения функции fibonacci_no_memoize: {end_time - start_time} секунд")


def run_fibonacci_with_memoize():
    start_time = time.time()
    fibonacci_with_memoize(130)
    end_time = time.time()
    print(f"Время выполнения функции fibonacci_with_memoize: {end_time - start_time} секунд")


run_fibonacci_with_memoize()
run_fibonacci_no_memoize()

