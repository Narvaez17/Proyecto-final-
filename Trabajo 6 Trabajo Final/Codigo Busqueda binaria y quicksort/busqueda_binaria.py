def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if lista[medio] == elemento:
            return medio
        elif elemento < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1
    
    return -1

def busqueda_simple(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

if __name__ == "__main__":
    numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Lista de números:", numeros)
    print()
    
    numero_buscado = 7
    
    resultado = busqueda_binaria(numeros, numero_buscado)
    if resultado != -1:
        print(f"¡Encontré el {numero_buscado} en la posición {resultado}!")
    else:
        print(f"No encontré el {numero_buscado}")
    
    resultado_simple = busqueda_simple(numeros, numero_buscado)
    if resultado_simple != -1:
        print(f"Búsqueda simple también lo encontró en la posición {resultado_simple}")
    
    print()
    numero_no_existe = 8
    resultado = busqueda_binaria(numeros, numero_no_existe)
    if resultado == -1:
        print(f"Correcto: el {numero_no_existe} no está en la lista") 