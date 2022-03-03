from numba import jit
import math
import random
import time


@jit(nopython=True)
def numba_basic_alg(n):
    for _ in range(n):
        x = random.random()
        y = random.random()
        a = random.random()
        t1 = math.sin(a) * x + math.cos(a) * y
        t2 = -math.cos(a) * x + math.sin(a) * y


def __main__():
    for i in range(0, 11):
        if i == 0:
            numba_basic_alg(int(i * 1e6))
            continue
        else:
            print("Iterations", i * 1e6)
            start = time.time()
            numba_basic_alg(int(i * 1e6))
            print(f'{(time.time() - start) * 1000:.2f} ms')


__main__()
