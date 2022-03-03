import math
import random
import time
from dataclasses import dataclass
import sys

from mpi4py import MPI

@dataclass
class DataDict:
    n:int
    k:int

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = int(sys.argv[1])

if rank == 0:
    data = DataDict(n=n, k=size)
    start = time.time()
    for i in range(size-1):
        comm.send(data,dest=i+1)
    for i in range(size-1):
        comm.recv(source=i+1)
    print('Iters:',n,'Threads:',size-1,'Time:',time.time()-start,'seconds')
if rank != 0:
    data:DataDict = comm.recv(source=0)
    for _ in range(int(data.n/data.k)):
        x = random.random()
        y = random.random()
        a = random.random()
        t1 = math.sin(a)*x + math.cos(a)*y
        t2 = -math.cos(a)*x + math.sin(a)*y
    comm.send('done',dest=0)