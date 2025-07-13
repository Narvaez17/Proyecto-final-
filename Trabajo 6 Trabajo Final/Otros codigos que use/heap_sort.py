def heap_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n // 2 - 1, -1, -1):
        hacer_heap(lista_copia, n, i)
    
    for i in range(n - 1, 0, -1):
        lista_copia[0], lista_copia[i] = lista_copia[i], lista_copia[0]
        hacer_heap(lista_copia, i, 0)
    
    return lista_copia

def hacer_heap(lista, tamaño, raiz):
    mas_grande = raiz
    hijo_izquierdo = 2 * raiz + 1
    hijo_derecho = 2 * raiz + 2
    
    if hijo_izquierdo < tamaño and lista[hijo_izquierdo] > lista[mas_grande]:
        mas_grande = hijo_izquierdo
    
    if hijo_derecho < tamaño and lista[hijo_derecho] > lista[mas_grande]:
        mas_grande = hijo_derecho
    
    if mas_grande != raiz:
        lista[raiz], lista[mas_grande] = lista[mas_grande], lista[raiz]
        hacer_heap(lista, tamaño, mas_grande)

def mostrar_heap(lista):
    n = len(lista)
    print("Heap como árbol:")
    nivel = 0
    elementos_en_nivel = 1
    i = 0
    
    while i < n:
        espacios = " " * (20 // (nivel + 1))
        for j in range(elementos_en_nivel):
            if i < n:
                print(f"{espacios}{lista[i]}", end=" ")
                i += 1
        print()
        
        nivel += 1
        elementos_en_nivel *= 2
        
        if i >= n:
            break

if __name__ == "__main__":
    numeros = [12, 11, 13, 5, 6, 7]
    
    print("Lista original:", numeros)
    print()
    
    print("Primero construimos el heap:")
    heap_ejemplo = numeros.copy()
    n = len(heap_ejemplo)
    
    for i in range(n // 2 - 1, -1, -1):
        hacer_heap(heap_ejemplo, n, i)
    
    print("Heap construido:", heap_ejemplo)
    mostrar_heap(heap_ejemplo)
    
    resultado = heap_sort(numeros)
    print()
    print("Después de aplicar Heap Sort:")
    print("Lista ordenada:", resultado)
