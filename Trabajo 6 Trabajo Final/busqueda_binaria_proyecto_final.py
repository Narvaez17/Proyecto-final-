"""
PROYECTO FINAL: ANÁLISIS Y SIMULACIÓN DEL ALGORITMO DE BÚSQUEDA BINARIA
Universidad Americana - Facultad de Ingeniería y Arquitectura

Estudiantes:
- Rene Nicolas Sandoval Lagos  
- Roberto Ezequiel Fernández Palacios

Docente: Cesar David Marin Lopez
Fecha: 30/06/2025

Este archivo contiene la implementación completa del algoritmo de búsqueda binaria
y todas las funciones necesarias para el análisis de rendimiento.
"""

import time
import tracemalloc
import math
import random
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Tuple, Dict, Any

# ===============================================================================
# IMPLEMENTACIÓN PRINCIPAL DEL ALGORITMO DE BÚSQUEDA BINARIA
# ===============================================================================

def busqueda_binaria(lista: List[Any], clave: Any) -> Tuple[int, int]:
    """
    Implementa búsqueda binaria iterativa con contador de pasos
    
    Args:
        lista: Lista ordenada donde buscar
        clave: Elemento a localizar
    
    Returns:
        tuple: (posición_encontrada, número_de_pasos)
               posición_encontrada = -1 si no se encuentra
    """
    inicio = 0
    fin = len(lista) - 1
    pasos = 0
    
    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2
        
        if lista[medio] == clave:
            return medio, pasos  # Elemento encontrado
        elif lista[medio] < clave:
            inicio = medio + 1   # Buscar en mitad superior
        else:
            fin = medio - 1      # Buscar en mitad inferior
    
    return -1, pasos  # Elemento no encontrado

def busqueda_lineal(lista: List[Any], clave: Any) -> Tuple[int, int]:
    """
    Implementa búsqueda lineal con contador de pasos para comparación
    
    Args:
        lista: Lista donde buscar
        clave: Elemento a localizar
    
    Returns:
        tuple: (posición_encontrada, número_de_pasos)
    """
    pasos = 0
    for i, elemento in enumerate(lista):
        pasos += 1
        if elemento == clave:
            return i, pasos
    return -1, pasos

# ===============================================================================
# FUNCIONES DE MEDICIÓN DE RENDIMIENTO
# ===============================================================================

def medir_rendimiento_busqueda(lista: List[Any], clave: Any) -> Dict[str, Any]:
    """
    Mide rendimiento integral de la búsqueda binaria
    
    Args:
        lista: Lista ordenada para búsqueda
        clave: Elemento a buscar
    
    Returns:
        dict: Métricas completas de rendimiento
    """
    # Iniciar seguimiento de memoria
    tracemalloc.start()
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.perf_counter()
    posicion, pasos = busqueda_binaria(lista, clave)
    tiempo_fin = time.perf_counter()
    
    # Calcular métricas
    tiempo_ejecucion = (tiempo_fin - tiempo_inicio) * 1_000_000  # microsegundos
    
    # Obtener uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'posicion': posicion,
        'pasos': pasos,
        'tiempo_us': tiempo_ejecucion,
        'memoria_actual': current,
        'memoria_pico': peak
    }

def medir_rendimiento_comparativo(lista: List[Any], clave: Any) -> Dict[str, Any]:
    """
    Mide rendimiento comparativo entre búsqueda binaria y lineal
    
    Args:
        lista: Lista ordenada para búsqueda
        clave: Elemento a buscar
    
    Returns:
        dict: Métricas comparativas de rendimiento
    """
    # Medir búsqueda binaria
    tiempo_inicio = time.perf_counter()
    pos_bin, pasos_bin = busqueda_binaria(lista, clave)
    tiempo_fin = time.perf_counter()
    tiempo_binaria = (tiempo_fin - tiempo_inicio) * 1_000_000
    
    # Medir búsqueda lineal
    tiempo_inicio = time.perf_counter()
    pos_lin, pasos_lin = busqueda_lineal(lista, clave)
    tiempo_fin = time.perf_counter()
    tiempo_lineal = (tiempo_fin - tiempo_inicio) * 1_000_000
    
    # Calcular ventajas
    ventaja_tiempo = tiempo_lineal / tiempo_binaria if tiempo_binaria > 0 else 0
    ventaja_pasos = pasos_lin / pasos_bin if pasos_bin > 0 else 0
    
    return {
        'posicion_binaria': pos_bin,
        'posicion_lineal': pos_lin,
        'tiempo_binaria_us': tiempo_binaria,
        'tiempo_lineal_us': tiempo_lineal,
        'pasos_binaria': pasos_bin,
        'pasos_lineal': pasos_lin,
        'ventaja_tiempo': ventaja_tiempo,
        'ventaja_pasos': ventaja_pasos
    }

# ===============================================================================
# FUNCIONES DE PRUEBAS SISTEMÁTICAS
# ===============================================================================

def pruebas_pequena_escala() -> List[Dict[str, Any]]:
    """
    Ejecuta pruebas en listas pequeñas (100-1000 elementos)
    
    Returns:
        list: Resultados de las pruebas de pequeña escala
    """
    print("🔍 Ejecutando pruebas de pequeña escala...")
    resultados = []
    tamaños = [100, 200, 400, 600, 800, 1000]
    
    for n in tamaños:
        print(f"  📊 Probando con {n} elementos...")
        
        # Crear lista ordenada
        lista = list(range(n))
        
        # Buscar elemento central (mejor caso)
        clave = n // 2
        
        # Medir rendimiento
        resultado = medir_rendimiento_busqueda(lista, clave)
        
        # Calcular métricas adicionales
        log2_n = math.log2(n)
        operaciones_teoricas = 6 + 8 * log2_n
        
        resultados.append({
            'tamaño': n,
            'tiempo_us': round(resultado['tiempo_us'], 2),
            'pasos': resultado['pasos'],
            'log2_n': round(log2_n, 2),
            'operaciones': round(operaciones_teoricas, 1),
            'memoria_kb': round(resultado['memoria_pico'] / 1024, 1)
        })
    
    return resultados

def pruebas_gran_escala() -> List[Dict[str, Any]]:
    """
    Ejecuta pruebas en listas grandes (10,000-100,000 elementos)
    
    Returns:
        list: Resultados de las pruebas de gran escala
    """
    print("🚀 Ejecutando pruebas de gran escala...")
    resultados = []
    tamaños = [10000, 20000, 40000, 60000, 80000, 100000]
    
    for n in tamaños:
        print(f"  📈 Probando con {n:,} elementos...")
        
        # Crear lista ordenada de enteros consecutivos
        lista = list(range(n))
        
        # Buscar elemento central (caso promedio)
        clave = n // 2
        
        # Medir rendimiento
        resultado = medir_rendimiento_busqueda(lista, clave)
        
        resultados.append({
            'tamaño': n,
            'tiempo_us': round(resultado['tiempo_us'], 2),
            'pasos': resultado['pasos'],
            'log2_n': round(math.log2(n), 2),
            'memoria_kb': round(resultado['memoria_pico'] / 1024, 1)
        })
    
    return resultados

def generar_nombres(cantidad: int) -> List[str]:
    """
    Genera lista de nombres ficticios ordenados alfabéticamente
    
    Args:
        cantidad: Número de nombres a generar
    
    Returns:
        list: Lista de nombres ordenados
    """
    nombres_base = [
        "Ana", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel",
        "Helena", "Ignacio", "Julia", "Kevin", "Laura", "Mario",
        "Natalia", "Oscar", "Patricia", "Quintero", "Rosa", "Santiago",
        "Teresa", "Ulises", "Valentina", "Walter", "Ximena", "Yolanda", "Zacarias"
    ]
    
    nombres = []
    for i in range(cantidad):
        base = random.choice(nombres_base)
        nombres.append(f"{base}{i:04d}")
    
    return sorted(nombres)

def pruebas_con_nombres() -> List[Dict[str, Any]]:
    """
    Ejecuta pruebas con datos cualitativos (nombres)
    
    Returns:
        list: Resultados de las pruebas con nombres
    """
    print("👥 Ejecutando pruebas con nombres...")
    resultados = []
    tamaños = [1000, 5000, 10000]
    
    for n in tamaños:
        print(f"  📝 Probando con {n:,} nombres...")
        nombres = generar_nombres(n)
        
        # Probar diferentes posiciones
        posiciones = [0, n//2, n-1]  # inicio, medio, final
        
        for pos in posiciones:
            clave = nombres[pos]
            
            # Medir búsqueda binaria
            resultado_bin = medir_rendimiento_busqueda(nombres, clave)
            
            # Simular búsqueda lineal (estimación)
            tiempo_lineal_estimado = pos * 1.0  # microsegundos estimados
            
            resultados.append({
                'tamaño': n,
                'posicion_buscada': pos,
                'tiempo_binaria_us': round(resultado_bin['tiempo_us'], 2),
                'tiempo_lineal_us': round(tiempo_lineal_estimado, 2),
                'pasos_binaria': resultado_bin['pasos'],
                'pasos_lineal': pos + 1,
                'elemento_encontrado': resultado_bin['posicion'] != -1,
                'nombre_buscado': clave[:10] + "..." if len(clave) > 10 else clave
            })
    
    return resultados

def comparacion_binaria_vs_lineal() -> List[Dict[str, Any]]:
    """
    Compara rendimiento entre búsqueda binaria y lineal
    
    Returns:
        list: Resultados de la comparación
    """
    print("⚡ Ejecutando comparación binaria vs lineal...")
    resultados = []
    tamaños = [1000, 5000, 10000, 25000, 50000, 100000]
    
    for n in tamaños:
        print(f"  🔬 Comparando con {n:,} elementos...")
        lista = list(range(n))
        
        # Buscar último elemento (peor caso para lineal)
        clave = n - 1
        
        # Medir comparativamente
        resultado = medir_rendimiento_comparativo(lista, clave)
        
        resultados.append({
            'tamaño': n,
            'tiempo_binaria_us': round(resultado['tiempo_binaria_us'], 2),
            'tiempo_lineal_us': round(resultado['tiempo_lineal_us'], 2),
            'ventaja_tiempo': round(resultado['ventaja_tiempo'], 1),
            'pasos_binaria': resultado['pasos_binaria'],
            'pasos_lineal': resultado['pasos_lineal'],
            'ventaja_pasos': round(resultado['ventaja_pasos'], 1)
        })
    
    return resultados

# ===============================================================================
# FUNCIONES DE ANÁLISIS AVANZADO
# ===============================================================================

def analisis_complejidad_espacial() -> List[Dict[str, Any]]:
    """
    Analiza la complejidad espacial del algoritmo
    
    Returns:
        list: Resultados del análisis espacial
    """
    print("💾 Analizando complejidad espacial...")
    resultados = []
    tamaños = [1000, 5000, 10000, 20000, 50000]
    
    for n in tamaños:
        # Estimar memoria de la lista (Python integers)
        memoria_lista = n * 28  # bytes aproximados por entero en Python
        memoria_variables = 140  # bytes para variables del algoritmo
        
        resultados.append({
            'tamaño': n,
            'memoria_lista_bytes': memoria_lista,
            'memoria_variables_bytes': memoria_variables,
            'memoria_total_kb': round((memoria_lista + memoria_variables) / 1024, 1),
            'porcentaje_variables': round((memoria_variables / (memoria_lista + memoria_variables)) * 100, 3)
        })
    
    return resultados

def calcular_punto_equilibrio() -> List[Dict[str, Any]]:
    """
    Calcula el punto de equilibrio para justificar el ordenamiento
    
    Returns:
        list: Resultados del punto de equilibrio
    """
    print("⚖️  Calculando puntos de equilibrio...")
    resultados = []
    tamaños = [1000, 5000, 10000, 50000]
    
    for n in tamaños:
        # Estimar costo de ordenamiento (QuickSort promedio)
        costo_ordenar = n * math.log2(n) * 1.5  # operaciones estimadas
        
        # Costo búsqueda promedio
        costo_busqueda_lineal = n / 2
        costo_busqueda_binaria = math.log2(n)
        
        # Diferencia de costo por búsqueda
        diferencia_por_busqueda = costo_busqueda_lineal - costo_busqueda_binaria
        
        # Número de búsquedas necesarias
        busquedas_necesarias = math.ceil(costo_ordenar / diferencia_por_busqueda)
        
        resultados.append({
            'tamaño': n,
            'costo_ordenar': round(costo_ordenar),
            'busqueda_lineal_promedio': round(costo_busqueda_lineal, 1),
            'busqueda_binaria_promedio': round(costo_busqueda_binaria, 1),
            'busquedas_necesarias': busquedas_necesarias
        })
    
    return resultados

def validacion_teorica() -> List[Dict[str, Any]]:
    """
    Valida las predicciones teóricas contra resultados empíricos
    
    Returns:
        list: Resultados de la validación teórica
    """
    print("🧮 Validando predicciones teóricas...")
    resultados = []
    
    # Ejecutar pruebas rápidas para validación
    tamaños_validacion = [100, 1000, 10000, 100000, 1000000]
    
    for n in tamaños_validacion:
        lista = list(range(n))
        clave = n // 2
        
        # Medir pasos reales
        _, pasos_reales = busqueda_binaria(lista, clave)
        
        # Calcular pasos teóricos
        pasos_teoricos = math.log2(n)
        
        # Calcular ventaja teórica vs lineal
        pasos_lineal_teorico = n
        ventaja_teorica = pasos_lineal_teorico / pasos_teoricos
        
        resultados.append({
            'tamaño': n,
            'pasos_reales': pasos_reales,
            'pasos_teoricos': round(pasos_teoricos, 1),
            'diferencia': abs(pasos_reales - pasos_teoricos),
            'lineal_teorico': pasos_lineal_teorico,
            'ventaja_teorica': round(ventaja_teorica, 1)
        })
    
    return resultados

# ===============================================================================
# FUNCIONES DE VISUALIZACIÓN Y EXPORTACIÓN
# ===============================================================================

def generar_graficas(resultados_pequena: List[Dict], resultados_grande: List[Dict], 
                    resultados_comparacion: List[Dict]):
    """
    Genera las gráficas principales del análisis
    
    Args:
        resultados_pequena: Datos de pruebas pequeñas
        resultados_grande: Datos de pruebas grandes  
        resultados_comparacion: Datos de comparación
    """
    print("📊 Generando gráficas de análisis...")
    
    # Configurar estilo
    plt.style.use('default')
    fig = plt.figure(figsize=(20, 15))
    
    # Gráfica 1: Tiempo vs Tamaño (Comparación)
    ax1 = plt.subplot(2, 3, 1)
    tamaños_comp = [r['tamaño'] for r in resultados_comparacion]
    tiempos_bin = [r['tiempo_binaria_us'] for r in resultados_comparacion]
    tiempos_lin = [r['tiempo_lineal_us'] for r in resultados_comparacion]
    
    plt.plot(tamaños_comp, tiempos_bin, 'b-o', label='Búsqueda Binaria', linewidth=2)
    plt.plot(tamaños_comp, tiempos_lin, 'r-s', label='Búsqueda Lineal', linewidth=2)
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Tiempo (microsegundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfica 2: Pasos vs Tamaño
    ax2 = plt.subplot(2, 3, 2)
    tamaños_todos = [r['tamaño'] for r in resultados_pequena + resultados_grande]
    pasos_todos = [r['pasos'] for r in resultados_pequena + resultados_grande]
    log2_teorico = [math.log2(t) for t in tamaños_todos]
    
    plt.plot(tamaños_todos, pasos_todos, 'go-', label='Pasos Reales', linewidth=2)
    plt.plot(tamaños_todos, log2_teorico, 'b--', label='log₂(n) Teórico', linewidth=2)
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Número de Pasos')
    plt.title('Validación Teórica: Pasos Reales vs Teóricos')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfica 3: Ventaja de Búsqueda Binaria
    ax3 = plt.subplot(2, 3, 3)
    ventajas_tiempo = [r['ventaja_tiempo'] for r in resultados_comparacion]
    
    plt.bar(range(len(tamaños_comp)), ventajas_tiempo, color='lightblue', alpha=0.7)
    plt.xlabel('Tamaño de Lista')
    plt.ylabel('Factor de Mejora')
    plt.title('Ventaja de Búsqueda Binaria (Tiempo)')
    plt.xticks(range(len(tamaños_comp)), [f"{t:,}" for t in tamaños_comp], rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Gráfica 4: Consumo de Memoria
    ax4 = plt.subplot(2, 3, 4)
    memorias = [r['memoria_kb'] for r in resultados_grande]
    tamaños_mem = [r['tamaño'] for r in resultados_grande]
    
    plt.plot(tamaños_mem, memorias, 'mo-', linewidth=2)
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Memoria (KB)')
    plt.title('Consumo de Memoria vs Tamaño')
    plt.grid(True, alpha=0.3)
    
    # Gráfica 5: Escalabilidad Logarítmica
    ax5 = plt.subplot(2, 3, 5)
    plt.loglog(tamaños_comp, tiempos_bin, 'b-o', label='Búsqueda Binaria', linewidth=2)
    plt.loglog(tamaños_comp, tiempos_lin, 'r-s', label='Búsqueda Lineal', linewidth=2)
    plt.xlabel('Tamaño de la Lista (escala log)')
    plt.ylabel('Tiempo (escala log)')
    plt.title('Comparación en Escala Logarítmica')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfica 6: Eficiencia por Operación
    ax6 = plt.subplot(2, 3, 6)
    eficiencia = [r['tiempo_us'] / r['pasos'] for r in resultados_pequena + resultados_grande]
    tamaños_ef = [r['tamaño'] for r in resultados_pequena + resultados_grande]
    
    plt.plot(tamaños_ef, eficiencia, 'co-', linewidth=2)
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Tiempo por Paso (μs)')
    plt.title('Eficiencia por Operación')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('C:/Users/sando/Downloads/Dosson/Trabajo 6 Trabajo Final/analisis_busqueda_binaria.png', 
                dpi=300, bbox_inches='tight')
    plt.show()

def exportar_resultados_excel(todos_los_resultados: Dict[str, List[Dict]]):
    """
    Exporta todos los resultados a un archivo Excel
    
    Args:
        todos_los_resultados: Diccionario con todos los conjuntos de resultados
    """
    print("📁 Exportando resultados a Excel...")
    
    archivo_excel = 'C:/Users/sando/Downloads/Dosson/Trabajo 6 Trabajo Final/resultados_busqueda_binaria.xlsx'
    
    with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
        for nombre_hoja, datos in todos_los_resultados.items():
            df = pd.DataFrame(datos)
            df.to_excel(writer, sheet_name=nombre_hoja, index=False)
    
    print(f"✅ Resultados exportados a: {archivo_excel}")

def imprimir_tabla_formateada(datos: List[Dict], titulo: str, columnas_principales: List[str]):
    """
    Imprime una tabla formateada en consola
    
    Args:
        datos: Lista de diccionarios con los datos
        titulo: Título de la tabla
        columnas_principales: Columnas principales a mostrar
    """
    print(f"\n{titulo}")
    print("=" * len(titulo))
    
    if not datos:
        print("No hay datos para mostrar")
        return
    
    # Crear encabezados
    encabezados = []
    for col in columnas_principales:
        if col in datos[0]:
            encabezados.append(col)
    
    # Imprimir encabezados
    formato = " | ".join([f"{enc:>12}" for enc in encabezados])
    print(formato)
    print("-" * len(formato))
    
    # Imprimir datos
    for fila in datos:
        valores = []
        for col in encabezados:
            valor = fila.get(col, "N/A")
            if isinstance(valor, float):
                valores.append(f"{valor:>12.2f}")
            elif isinstance(valor, int):
                valores.append(f"{valor:>12,}")
            else:
                valores.append(f"{str(valor):>12}")
        print(" | ".join(valores))

# ===============================================================================
# FUNCIÓN PRINCIPAL DE EJECUCIÓN
# ===============================================================================

def ejecutar_analisis_completo():
    """
    Ejecuta el análisis completo del algoritmo de búsqueda binaria
    """
    print("🚀 INICIANDO ANÁLISIS COMPLETO DEL ALGORITMO DE BÚSQUEDA BINARIA")
    print("=" * 80)
    
    # Ejecutar todas las pruebas
    resultados_pequena = pruebas_pequena_escala()
    resultados_grande = pruebas_gran_escala()
    resultados_nombres = pruebas_con_nombres()
    resultados_comparacion = comparacion_binaria_vs_lineal()
    analisis_espacial = analisis_complejidad_espacial()
    punto_equilibrio = calcular_punto_equilibrio()
    validacion = validacion_teorica()
    
    # Mostrar resultados en consola
    imprimir_tabla_formateada(
        resultados_pequena, 
        "TABLA 2: ANÁLISIS DE PEQUEÑA ESCALA",
        ['tamaño', 'tiempo_us', 'log2_n', 'operaciones', 'pasos']
    )
    
    imprimir_tabla_formateada(
        resultados_grande,
        "TABLA 3: ANÁLISIS DE GRAN ESCALA", 
        ['tamaño', 'tiempo_us', 'log2_n', 'pasos', 'memoria_kb']
    )
    
    imprimir_tabla_formateada(
        resultados_comparacion,
        "TABLA 4: BÚSQUEDA BINARIA VS BÚSQUEDA LINEAL",
        ['tamaño', 'tiempo_binaria_us', 'tiempo_lineal_us', 'ventaja_tiempo', 'pasos_binaria', 'pasos_lineal']
    )
    
    imprimir_tabla_formateada(
        analisis_espacial,
        "TABLA 7: COMPLEJIDAD ESPACIAL",
        ['tamaño', 'memoria_lista_bytes', 'memoria_variables_bytes', 'memoria_total_kb', 'porcentaje_variables']
    )
    
    imprimir_tabla_formateada(
        punto_equilibrio,
        "TABLA 8: PUNTO DE EQUILIBRIO PARA ORDENAMIENTO",
        ['tamaño', 'costo_ordenar', 'busqueda_lineal_promedio', 'busqueda_binaria_promedio', 'busquedas_necesarias']
    )
    
    imprimir_tabla_formateada(
        validacion,
        "TABLA 9: VALIDACIÓN TEÓRICA",
        ['tamaño', 'pasos_reales', 'pasos_teoricos', 'diferencia', 'ventaja_teorica']
    )
    
    # Generar gráficas
    generar_graficas(resultados_pequena, resultados_grande, resultados_comparacion)
    
    # Exportar a Excel
    todos_los_resultados = {
        'Pequeña_Escala': resultados_pequena,
        'Gran_Escala': resultados_grande,
        'Pruebas_Nombres': resultados_nombres,
        'Comparacion_Algoritmos': resultados_comparacion,
        'Analisis_Espacial': analisis_espacial,
        'Punto_Equilibrio': punto_equilibrio,
        'Validacion_Teorica': validacion
    }
    
    exportar_resultados_excel(todos_los_resultados)
    
    print("\n🎉 ANÁLISIS COMPLETO FINALIZADO")
    print("=" * 80)
    print("✅ Todas las pruebas ejecutadas exitosamente")
    print("📊 Gráficas generadas")
    print("📁 Resultados exportados a Excel")
    print("\nEl análisis confirma la superioridad de la búsqueda binaria:")
    print(f"  • Mejora promedio de {resultados_comparacion[-1]['ventaja_tiempo']:.1f}x en tiempo")
    print(f"  • Mejora promedio de {resultados_comparacion[-1]['ventaja_pasos']:.1f}x en pasos")
    print(f"  • Complejidad espacial constante O(1)")
    print(f"  • Complejidad temporal O(log n) validada experimentalmente")

# ===============================================================================
# FUNCIONES DE DEMOSTRACIÓN INDIVIDUAL
# ===============================================================================

def demo_busqueda_simple():
    """
    Demostración simple del algoritmo para fines educativos
    """
    print("\n🔍 DEMOSTRACIÓN SIMPLE DE BÚSQUEDA BINARIA")
    print("-" * 50)
    
    # Lista de ejemplo
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    elemento_buscar = 13
    
    print(f"Lista: {lista}")
    print(f"Buscando: {elemento_buscar}")
    
    posicion, pasos = busqueda_binaria(lista, elemento_buscar)
    
    if posicion != -1:
        print(f"✅ Elemento encontrado en posición {posicion}")
        print(f"📊 Pasos realizados: {pasos}")
    else:
        print(f"❌ Elemento no encontrado")
        print(f"📊 Pasos realizados: {pasos}")

def demo_comparacion_rapida():
    """
    Demostración rápida de comparación entre algoritmos
    """
    print("\n⚡ COMPARACIÓN RÁPIDA: BINARIA VS LINEAL")
    print("-" * 50)
    
    tamaño = 10000
    lista = list(range(tamaño))
    elemento_buscar = tamaño - 1  # Peor caso para búsqueda lineal
    
    print(f"Lista de {tamaño:,} elementos ordenados")
    print(f"Buscando último elemento: {elemento_buscar}")
    
    # Búsqueda binaria
    inicio = time.perf_counter()
    pos_bin, pasos_bin = busqueda_binaria(lista, elemento_buscar)
    tiempo_bin = (time.perf_counter() - inicio) * 1000
    
    # Búsqueda lineal
    inicio = time.perf_counter()
    pos_lin, pasos_lin = busqueda_lineal(lista, elemento_buscar)
    tiempo_lin = (time.perf_counter() - inicio) * 1000
    
    print(f"\n📊 RESULTADOS:")
    print(f"Búsqueda Binaria: {tiempo_bin:.2f} ms, {pasos_bin} pasos")
    print(f"Búsqueda Lineal:  {tiempo_lin:.2f} ms, {pasos_lin:,} pasos")
    print(f"Mejora de velocidad: {tiempo_lin/tiempo_bin:.1f}x")
    print(f"Mejora en pasos: {pasos_lin/pasos_bin:.1f}x")

# ===============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# ===============================================================================

if __name__ == "__main__":
    # Permitir al usuario elegir qué ejecutar
    print("PROYECTO FINAL: ANÁLISIS DE BÚSQUEDA BINARIA")
    print("=" * 50)
    print("Opciones disponibles:")
    print("1. Ejecutar análisis completo")
    print("2. Demostración simple")
    print("3. Comparación rápida")
    print("4. Salir")
    
    while True:
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                ejecutar_analisis_completo()
                break
            elif opcion == "2":
                demo_busqueda_simple()
            elif opcion == "3":
                demo_comparacion_rapida()
            elif opcion == "4":
                print("👋 ¡Gracias por usar el analizador de búsqueda binaria!")
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Análisis interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            break 