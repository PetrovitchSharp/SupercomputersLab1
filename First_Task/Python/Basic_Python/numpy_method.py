import numpy as np
import time


def numpy_alg(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    a = np.random.rand(n)
    t1 = np.sin(a) * x + np.cos(a) * y
    t2 = -np.cos(a) * x + np.sin(a) * y


def __main__():
    for i in range(1, 11):
        print("Iterations", i * 1e6)
        start = time.time()
        numpy_alg(int(i * 1e6))
        print(f'{(time.time() - start) * 1000:.2f} ms')


__main__()
