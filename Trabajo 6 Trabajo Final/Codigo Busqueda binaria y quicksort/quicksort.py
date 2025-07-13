def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[-1]
    
    menores = []
    mayores = []
    
    for elemento in lista[:-1]:
        if elemento <= pivote:
            menores.append(elemento)
        else:
            mayores.append(elemento)
    
    return quicksort(menores) + [pivote] + quicksort(mayores)

def ordenamiento_burbuja(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", numeros)
    print()
    
    resultado_quick = quicksort(numeros)
    print("Ordenado con QuickSort:", resultado_quick)
    
    resultado_burbuja = ordenamiento_burbuja(numeros)
    print("Ordenado con burbuja:", resultado_burbuja)
    

    print()
    numeros_grandes = [3, 6, 8, 10, 1, 2, 1]
    print("Lista más grande:", numeros_grandes)
    print("Ordenada:", quicksort(numeros_grandes))
    
    print()
    print("¿Cómo funciona QuickSort paso a paso?")
    print("Lista: [3, 6, 8, 10, 1, 2, 1]")
    print("1. Pivote = 1 (último elemento)")
    print("2. Menores que 1: [] (no hay)")
    print("3. Mayores que 1: [3, 6, 8, 10, 1, 2]")
    print("4. Se repite el proceso con cada parte...")
    print("5. Al final se juntan todas las partes ordenadas") 