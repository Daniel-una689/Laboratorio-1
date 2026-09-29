import random
import time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


def medir_tiempo(nombre, lista):
    copia = lista[:]  # usa una copia para no modificar la original
    inicio = time.perf_counter()  # inicio de medición
    heap_sort(copia)             # ejecución del algoritmo
    fin = time.perf_counter()     # fin de medición

    tiempo_ms = (fin - inicio) * 1000
    print(f"{nombre:20} -> {tiempo_ms:.6f} ms")
    return tiempo_ms


def main():
    # --------------------------
    # Listas normales por tamaño
    # --------------------------
    lista100 = [random.randint(1, 10000) for _ in range(100)]
    lista500 = [random.randint(1, 10000) for _ in range(500)]
    lista1000 = [random.randint(1, 10000) for _ in range(2000)]
    lista5000 = [random.randint(1, 10000) for _ in range(5000)]

    # --------------------------
    # Casos A, B, C
    # --------------------------
    # Caso A. Lista aleatoria
    # usa random.sample para que no haya valores repetidos
    casoA_100 = random.sample(range(1, 10000), 100)
    casoA_500 = random.sample(range(1, 10000), 500)
    casoA_1000 = random.sample(range(1, 10000), 2000)
    casoA_5000 = random.sample(range(1, 10000), 5000)

    # Caso B. Lista ordenada
    casoB_100 = list(range(100))
    casoB_500 = list(range(500))
    casoB_1000 = list(range(2000))
    casoB_5000 = list(range(5000))

    # Caso C. Lista ordenada inversamente
    casoC_100 = list(range(100, 0, -1))
    casoC_500 = list(range(500, 0, -1))
    casoC_1000 = list(range(2000, 0, -1))
    casoC_5000 = list(range(5000, 0, -1))

    print("MEDICION DE TIEMPO HEAP SORT")
    print("=" * 60)

    # Medir listas normales
    medir_tiempo("lista100", lista100)
    medir_tiempo("lista500", lista500)
    medir_tiempo("lista1000", lista1000)
    medir_tiempo("lista5000", lista5000)

    print("-" * 60)

    # Medir Caso A
    medir_tiempo("A_100", casoA_100)
    medir_tiempo("A_500", casoA_500)
    medir_tiempo("A_1000", casoA_1000)
    medir_tiempo("A_5000", casoA_5000)

    print("-" * 60)

    # Medir Caso B
    medir_tiempo("B_100", casoB_100)
    medir_tiempo("B_500", casoB_500)
    medir_tiempo("B_1000", casoB_1000)
    medir_tiempo("B_5000", casoB_5000)

    print("-" * 60)

    # Medir Caso C
    medir_tiempo("C_100", casoC_100)
    medir_tiempo("C_500", casoC_500)
    medir_tiempo("C_1000", casoC_1000)
    medir_tiempo("C_5000", casoC_5000)


if __name__ == "__main__":
    main()