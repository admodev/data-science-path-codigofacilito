import numpy as np

np.array([1, 2, 3, 4 , 5])
a = np.array([1, 2, 3, 4 , 5])
print(a)
type(a)
print(a.size)
print(a.ndim)
print(a.dtype)
print(a.shape)
print(a + 10)
print(a - 10)
print(a * 10)
print(a / 10)
b = np.array([6, 7, 8, 9, 10])
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

c = np.array([1, 2, 3, 4, 5], dtype=float)

print(c)

d = np.array([1, 2, 3, 4, 5], dtype=str)

print(d)

e = np.array([1, 2, 3, 4, 5], dtype=bool)

print(e)

f = np.array([0, 0, 1, 1, 1], dtype=bool)

print(f)

g = np.array([1, 2, 3, 4, 5], dtype=complex)

print(g)

# Metodos arrays
arng = np.arange(0, 100)

print(arng)

# arange con saltos de 2 en 2
arng_step = np.arange(0, 20, 2)

print(arng_step)

# Prueba de sucesion de fibonacci
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def recursividad(arr):
    for x in range(len(arr)):
        print(fib(x))

print(recursividad(arng_step))

# Array de fixed type con placeholders
# muy util para hacer arrays de verdadero ( 1 ) y falso ( 0 )
empty_arr = np.zeros(10)

print(empty_arr)

# con tipo de dato
empty_arr_type = np.zeros(10, dtype=int)

print(empty_arr_type.dtype)

# lo mismo pero con unos...
empty_arr_one = np.ones(10, dtype=int)

print(empty_arr_one)

print(empty_arr_one.dtype)

# Crear array vacio con datos basura
trashed_memory = np.empty(10)

print(trashed_memory)

# y con tipo de dato
trashed_memory_type = np.empty(10, dtype=int)

print(trashed_memory_type)

# Array en a partir de numeros enteros aleatorios
random_int_array = np.random.randint(0, 100, 50)

print(random_int_array)
