def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)
    
    return juntar(izquierda_ordenada, derecha_ordenada)

def juntar(izquierda, derecha):
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

if __name__ == "__main__":
    numeros = [38, 27, 43, 3, 9, 82, 10]
    
    print("Lista original:", numeros)
    print()
    
    resultado = merge_sort(numeros)
    print("Ordenado con Merge Sort:", resultado)
    

    print()
    print("Ejemplo de juntar dos listas ordenadas:")
    lista1 = [1, 3, 5]
    lista2 = [2, 4, 6]
    resultado_juntar = juntar(lista1, lista2)
    print(f"Juntar {lista1} y {lista2} = {resultado_juntar}")
    
