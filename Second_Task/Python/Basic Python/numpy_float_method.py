import numpy as np
import time

total_memory = 2 * 1024 * 1024 * 1024 # 2GB of memory

def numpy_float_alg(size: int):
    a: np.ndarray[np.float_] = np.random.rand(int(size / 2 / 8))
    b: np.ndarray[np.float_] = np.random.rand(int(size / 2 / 8))
    a + b

def __main__():
    size: int = 1
    while (size <= total_memory):
        if (size == 1):
            numpy_float_alg(size)
            size = 1024 * 1024 * 4
            continue
        else:
            print("Size: ", int(size) / 2 / 8, "elements (", size / 1024 / 1024, "MB )")
            start: float = time.time()
            numpy_float_alg(size)
            size *= 2
            print(time.time() - start, "s")

__main__()