#region Preparations
import os
import pathlib

# Путь к корневой папке
root = pathlib.Path().resolve()

#endregion

#region Task 1

print("___________________________")
print("Task 1")
print("___________________________")

#region Standard Python Interpreter
# Запуск алгоритмов с использованием стандартного интерпретатора Python 3.8
os.chdir(f'{root}\\python\\basic python')

print("___________________________")
print("Standard Python Interpreter")
print("___________________________")

print("___________________________")
print("Basic Algorithm")
print("___________________________")
os.system('python basic_method.py')

print("___________________________")
print("One-Time-Assignment Algorithm")
print("___________________________")
os.system('python one_time_method.py')

print("___________________________")
print("Numpy Algorithm")
print("___________________________")
os.system('python numpy_method.py')

#endregion

#region Pypy JIT Compilation
# Запуск алгоритмов с использованием JIT компилятора Pypy
print("___________________________")
print("Pypy JIT Compilation")
print("___________________________")

print("___________________________")
print("Basic Algorithm")
print("___________________________")
os.system('pypy basic_method.py')

print("___________________________")
print("One-Time-Assignment Algorithm")
print("___________________________")
os.system('pypy one_time_method.py')

print("___________________________")
print("Numpy Algorithm")
print("___________________________")
os.system('pypy numpy_method.py')

#endregion

#region Numba JIT Compilation
# Запуск алгоритмов с использованием JIT компилятора Numba
os.chdir(f'{root}\\numba')

print("___________________________")
print("Numba JIT Compilation")
print("___________________________")

print("___________________________")
print("Basic Algorithm")
print("___________________________")
os.system('python basic_method.py')

print("___________________________")
print("One-Time-Assignment Algorithm")
print("___________________________")
os.system('python one_time_method.py')

print("___________________________")
print("Numpy Algorithm")
print("___________________________")
os.system('python numpy_method.py')

#endregion

#region MPI
# Запуск параллельных MPI алгоритмов
os.chdir(f'{root}\\python\\mpi')

print("___________________________")
print("MPI Execution")
print("___________________________")

print("___________________________")
print("Parallelization of internal computing")
print("___________________________")
for j in range(1, 11):
    os.system(f'mpiexec -n 3 python mpi_first_method.py {int(j * 1e6)}')

print("___________________________")
print("Parallelization of the external loop")
print("___________________________")
for i in range(3, 10, 2):
    for j in range(1, 11):
        os.system(f'mpiexec -n {i} python mpi_second_method.py {int(j * 1e6)}')

#endregion

#endregion