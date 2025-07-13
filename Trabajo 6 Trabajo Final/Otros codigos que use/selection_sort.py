def selection_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        indice_minimo = i
        
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[indice_minimo]:
                indice_minimo = j
        
        lista_copia[i], lista_copia[indice_minimo] = lista_copia[indice_minimo], lista_copia[i]
    
    return lista_copia

def selection_sort_paso_a_paso(lista):
    print("Selection Sort paso a paso:")
    print("Lista original:", lista)
    print()
    
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        print(f"Paso {i + 1}:")
        print(f"  Buscando el menor elemento desde la posición {i}")
        
        indice_minimo = i
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[indice_minimo]:
                indice_minimo = j
        
        print(f"  El menor elemento es {lista_copia[indice_minimo]} en la posición {indice_minimo}")
        
        if indice_minimo != i:
            print(f"  Intercambiando {lista_copia[i]} con {lista_copia[indice_minimo]}")
            lista_copia[i], lista_copia[indice_minimo] = lista_copia[indice_minimo], lista_copia[i]
        else:
            print(f"  {lista_copia[i]} ya está en la posición correcta")
        
        print(f"  Lista actual: {lista_copia}")
        print(f"  Parte ordenada: {lista_copia[:i+1]}")
        print()
    
    return lista_copia

def comparar_con_burbuja(lista):
    print("Comparación con Bubble Sort:")
    print("Lista original:", lista)
    print()
    
    resultado_selection = selection_sort(lista)
    print("Selection Sort resultado:", resultado_selection)
    
    def bubble_sort(lista):
        lista_copia = lista.copy()
        n = len(lista_copia)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista_copia[j] > lista_copia[j + 1]:
                    lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
        
        return lista_copia
    
    resultado_burbuja = bubble_sort(lista)
    print("Bubble Sort resultado:", resultado_burbuja)
    

if __name__ == "__main__":
    numeros = [64, 25, 12, 22, 11]
    
 
    print()
    print("Ejemplo con lista más grande:")
    numeros_grandes = [7, 3, 9, 1, 5, 2, 8, 4, 6]
    print("Original:", numeros_grandes)
    print("Ordenado:", selection_sort(numeros_grandes)) 