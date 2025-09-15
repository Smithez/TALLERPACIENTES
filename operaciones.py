import numpy as np

# 1. CREAR ARREGLOS--
arreglo1 = np.array([2, 4, 6, 8, 10])
arreglo2 = np.ones((4, 4))      # Matriz 4x4 de unos
arreglo3 = np.zeros((2, 2, 2))  # Arreglo 3D de ceros

# 2. IMPRIMIR ARREGLOS
print("=== Arreglo 1 (valores) ===")
for x in arreglo1:
    print(x)

print("\n=== Arreglo 2 (matriz de unos) ===")
for y in arreglo2:
    print(y)

print("\n=== Arreglo 3 (matriz 3D de ceros) ===")
for z in arreglo3:
    print(z)

# 3. OPERACIONES ESTADÍSTICAS
maximo = np.max(arreglo1)
minimo = np.min(arreglo1)
media  = np.mean(arreglo1)
posmax = np.argmax(arreglo1)  # índice del máximo
posmin = np.argmin(arreglo1)  # índice del mínimo

print("\n=== Operaciones con arreglo1 ===")
print("Máximo = ", maximo)
print("Mínimo = ", minimo)
print("Media  = ", media)
print("Posición del máximo = ", posmax)
print("Posición del mínimo = ", posmin)

# 4. OPERACIONES ENTRE ARREGLOS
arreglo4 = np.array([1, 2, 3, 4, 5])
arreglo6 = np.sum(arreglo1 * arreglo4)  # suma elemento a elemento

print("\n=== Operaciones entre arreglos ===")
print("Arreglo1 * Arreglo4 = ", arreglo1 * arreglo4)
print("Suma de productos = ", arreglo6)
