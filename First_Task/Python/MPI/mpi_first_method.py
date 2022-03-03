import math
import random
import time
from dataclasses import dataclass
import sys

from mpi4py import MPI


@dataclass
class DataDict:
    x: float
    y: float
    a: float
    iter: int


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = int(sys.argv[1])

if rank == 0:
    start = time.time()
    for i in range(n):
        x = random.random()
        y = random.random()
        a = random.random()
        data = DataDict(x=x, y=y, a=a, iter=i)

        comm.send(data, dest=1)
        comm.send(data, dest=2)

        t1 = comm.recv(source=1)
        t2 = comm.recv(source=2)
    print(f'Iters: {n} Threads: {size - 1} Time: {(time.time() - start) * 1000:.2f} ms')

if rank == 1:
    while True:
        data: DataDict = comm.recv(source=0)
        a: float = data.a
        x: float = data.x
        y: float = data.y
        t1 = math.sin(a) * x + math.cos(a) * y
        comm.send(t1, dest=0)
        if data.iter == n - 1:
            break
if rank == 2:
    while True:
        data: DataDict = comm.recv(source=0)
        a: float = data.a
        x: float = data.x
        y: float = data.y
        t2 = -math.cos(a) * x + math.sin(a) * y
        comm.send(t2, dest=0)
        if data.iter == n - 1:
            break

comm.Barrier()
MPI.Finalize()
