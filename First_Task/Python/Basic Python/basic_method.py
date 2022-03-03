import math
import random
import time

def basic_alg(n):
    for _ in range(n):
        x = random.random()
        y = random.random()
        a = random.random()
        t1 = math.sin(a)*x + math.cos(a)*y
        t2 = -math.cos(a)*x + math.sin(a)*y

def __main__():
    for i in range(1, 11):
        print("Iterations", i * 1e6)
        start = time.time()
        basic_alg(int(i * 1e6))
        print(time.time()-start,"s")

__main__()