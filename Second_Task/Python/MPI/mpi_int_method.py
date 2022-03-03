import random
import time
from dataclasses import dataclass
import sys
from typing import List

from mpi4py import MPI
from mpi4py.MPI import Intracomm


@dataclass
class Arrays:
    a: List[int]
    b: List[int]


def create_int_array(size: int):
    a: List[int] = []
    for _ in range(int(size)):
        a.append(random.randint(-10, 10))
    return a


comm: Intracomm = MPI.COMM_WORLD
size: int = comm.Get_size()
rank: int = comm.Get_rank()

n: int = int(sys.argv[1])

if rank == 0:

    start: float = time.time()
    a: List[int] = create_int_array(n)
    b: List[int] = create_int_array(n)
    c: List[int] = []

    for i in range(size - 1):
        data: Arrays = Arrays(
            a=a[int(i * (n / (size - 1))):int((i + 1) * (n / (size - 1)))],
            b=b[int(i * (n / (size - 1))):int((i + 1) * (n / (size - 1)))]
        )
        comm.send(data, dest=i + 1)

    for i in range(size - 1):
        res: List[int] = comm.recv(source=i + 1)
        c += res

    print(f'Size: {n / 2 / 8} elements ({n / 1024 / 1024 / 2} MB)')
    print(f'Time: {(time.time() - start) * 1000:.2f} ms on {size - 1} threads')

if rank != 0:
    data: Arrays = comm.recv(source=0)

    sub_c: List[int] = []
    for i in range(len(data.a)):
        sub_c.append(data.a[i] + data.b[i])

    comm.send(sub_c, dest=0)

MPI.Finalize()
