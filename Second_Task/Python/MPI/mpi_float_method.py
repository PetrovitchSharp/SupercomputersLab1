import random
import time
from dataclasses import dataclass
import sys
from typing import List

from mpi4py import MPI
from mpi4py.MPI import Intracomm


@dataclass
class Arrays:
    a: list
    b: list
    n: int


def create_float_array(size: int):
    a: List[float] = []
    for _ in range(int(size)):
        a.append(random.random())
    return a


comm: Intracomm = MPI.COMM_WORLD
size: int = comm.Get_size()
rank: int = comm.Get_rank()

n: int = int(sys.argv[1])

if rank == 0:

    start: float = time.time()
    a: List[float] = create_float_array(n)
    b: List[float] = create_float_array(n)
    c: List[float] = []
    data: Arrays = Arrays(a=a, b=b, n=n)

    for i in range(size - 1):
        comm.send(data, dest=i + 1)

    for i in range(size - 1):
        res: List[float] = comm.recv(source=i + 1)
        c += res

    print(f'Size: {n} elements ({n / 1024 / 1024} MB)')
    print(f'Time: {(time.time() - start) * 1000:.2f} ms on {size - 1} threads')

if rank != 0:
    data: Arrays = comm.recv(source=0)
    sub_a: List[float] = data.a[int((rank - 1) * (n / (size - 1))):int((rank - 1) * (n / (size - 1) + 1))]
    sub_b: List[float] = data.b[int((rank - 1) * (n / (size - 1))):int((rank - 1) * (n / (size - 1) + 1))]

    sub_c: List[float] = []
    for i in range(len(sub_a)):
        sub_c.append(sub_a[i] + sub_b[i])

    comm.send(sub_c, dest=0)

MPI.Finalize()
