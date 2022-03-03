# region Preparations
import os
import pathlib

# Путь к корневой папке
root = pathlib.Path().resolve()

# endregion

# region Task 1

print("___________________________")
print("Task 2")
print("___________________________")

# region Standard Python Interpreter
# Запуск алгоритмов с использованием стандартного интерпретатора Python 3.8
os.chdir(f'{root}\\python\\basic python')

print("___________________________")
print("Standard Python Interpreter")
print("___________________________")

print("___________________________")
print("Basic Int Algorithm")
print("___________________________")
os.system('python basic_int_method.py')

print("___________________________")
print("Basic Float Algorithm")
print("___________________________")
os.system('python basic_float_method.py')

print("___________________________")
print("Numpy Int Algorithm")
print("___________________________")
os.system('python numpy_int_method.py')

print("___________________________")
print("Numpy Float Algorithm")
print("___________________________")
os.system('python numpy_float_method.py')

# endregion

# region Pypy JIT Compilation
# Запуск алгоритмов с использованием JIT компилятора Pypy
print("___________________________")
print("Pypy JIT Compilation")
print("___________________________")

print("___________________________")
print("Basic Int Algorithm")
print("___________________________")
os.system('pypy basic_int_method.py')

print("___________________________")
print("Basic Float Algorithm")
print("___________________________")
os.system('pypy basic_float_method.py')

print("___________________________")
print("Numpy Int Algorithm")
print("___________________________")
os.system('pypy numpy_int_method.py')

print("___________________________")
print("Numpy Float Algorithm")
print("___________________________")
os.system('pypy numpy_float_method.py')

# endregion

# region Numba JIT Compilation
# Запуск алгоритмов с использованием JIT компилятора Numba
os.chdir(f'{root}\\numba')

print("___________________________")
print("Numba JIT Compilation")
print("___________________________")

print("___________________________")
print("Basic Int Algorithm")
print("___________________________")
os.system('python basic_int_method.py')

print("___________________________")
print("Basic Float Algorithm")
print("___________________________")
os.system('python basic_float_method.py')

print("___________________________")
print("Numpy Int Algorithm")
print("___________________________")
os.system('python numpy_int_method.py')

print("___________________________")
print("Numpy Float Algorithm")
print("___________________________")
os.system('python numpy_float_method.py')

# endregion

# region MPI
# Запуск параллельных MPI алгоритмов
os.chdir(f'{root}\\python\\mpi')
total_memory = 2 * 1024 * 1024 * 1024

print("___________________________")
print("MPI Execution")
print("___________________________")

print("___________________________")
print("Integer Arrays")
print("___________________________")
for i in range(3, 10, 2):
    size = 1024 * 1024 * 4
    while size <= total_memory:
        os.system(f'mpiexec -n {i} python mpi_int_method.py {int(size)}')
        size *= 2

print("___________________________")
print("Float Arrays")
print("___________________________")
for i in range(3, 10, 2):
    size = 1024 * 1024 * 4
    while size <= total_memory:
        os.system(f'mpiexec -n {i} python mpi_float_method.py {int(size)}')
        size *= 2

# endregion

# endregion
