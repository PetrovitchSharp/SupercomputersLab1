import math
import random
import time


def one_time_alg(n):
    for _ in range(n):
        x = random.random()
        y = random.random()
        a = random.random()
        _sin = math.sin(a)
        _cos = math.cos(a)
        t1 = _sin * x + _cos * y
        t2 = -_cos * x + _sin * y


def __main__():
    for i in range(1, 11):
        print("Iterations", i * 1e6)
        start = time.time()
        one_time_alg(int(i * 1e6))
        print(f'{(time.time() - start) * 1000:.2f} ms')


__main__()
