import random
import time
from numba import jit
from typing import List

total_memory: int = 2 * 1024 * 1024 * 1024 # 2GB of memory

@jit(nopython = True)
def create_float_array(size: int):
    a: List[float] = []
    for _ in range(int(size)):
        a.append(random.random())
    return a

@jit(nopython = True)
def add_arrays(a: List[float], b: List[float], size: int):
    c: List[float] = []
    for i in range(int(size)):
        c.append(a[i]+b[i])

@jit(nopython = True)
def basic_float_alg(size: int):
    a: List[float] = create_float_array(int(size / 2 / 8))
    b: List[float] = create_float_array(int(size / 2 / 8))
    add_arrays(a, b, int(size / 2 / 8))

def __main__():
    size: int = 1
    while (size <= total_memory):
        if (size == 1):
            basic_float_alg(size)
            size = 1024 * 1024 * 4
            continue
        else:
            print("Size: ", int(size) / 2 / 8, "elements (", size / 1024 / 1024, "MB )")
            start: float = time.time()
            basic_float_alg(size)
            size *= 2
            print(time.time() - start, "s")

__main__()