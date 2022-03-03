import random
import time
from typing import List

total_memory: int = 2 * 1024 * 1024 * 1024 # 2GB of memory

def create_int_array(size: int):
    a: List[int] = []
    for _ in range(int(size)):
        a.append(random.randint(-10,10))
    return a

def add_arrays(a: List[int], b: List[int], size: int):
    c: List[int] = []
    for i in range(int(size)):
        c.append(a[i]+b[i])

def basic_int_alg(size: int):
    a: List[int] = create_int_array(int(size / 2 / 8))
    b: List[int] = create_int_array(int(size / 2 / 8))
    add_arrays(a, b, int(size / 2 / 8))

def __main__():
    size: int = 1
    while (size <= total_memory):
        if (size == 1):
            basic_int_alg(size)
            size = 1024 * 1024 * 4
            continue
        else:
            print("Size: ", int(size) / 2 / 8, "elements (", size / 1024 / 1024 / 2, "MB )")
            start: float = time.time()
            basic_int_alg(size)
            size *= 2
            print(time.time() - start, "s")

__main__()