import numpy as np
import time
from numba import jit

total_memory: int = 2 * 1024 * 1024 * 1024 # 2GB of memory

@jit(nopython = True)
def numpy_int_alg(size: int):
    a: np.ndarray[np.int_] = np.random.randint(-10,10,int(size / 2 / 8))
    b: np.ndarray[np.int_] = np.random.randint(-10,10,int(size / 2 / 8))
    a + b

def __main__():
    size: int = 1
    while (size <= total_memory):
        if (size == 1):
            numpy_int_alg(size)
            size = 1024 * 1024 * 4
            continue
        else:
            print("Size: ", int(size) / 2 / 8, "elements (", size / 1024 / 1024 / 2, "MB )")
            start: float = time.time()
            numpy_int_alg(size)
            size *= 2
            print(time.time() - start, "s")

__main__()