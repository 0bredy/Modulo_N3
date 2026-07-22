# Modulo N3
# Practica N3 - Parte N2
# Estudiante: Bredy Guerra
import sys
from math import sqrt, ceil, floor, log
from re import match, search, findall
from collections import Counter
import pandas as pd

## Ejercicio N1: Lectura del archivo (sys + Pandas)
#A) Recibiendo Nombre de Archivo de la Consola
if len(sys.argv) < 2:
    nombre_archivo = None
else:
    nombre_archivo = sys.argv[1]

#B) Utilizando pandas para leer el archivo
def leer_archivo(nombre_archivo):
    """Verifica que exista el nombre de archivo y lo lee con pandas. 
        Devuelve el DataFrame o None si hay error."""
    if nombre_archivo is None:
        print("\nArchivo no especificado, utiliza el comando:\npython analizador_dataset.py archivo.csv")
        return None
    try:
        df = pd.read_csv(nombre_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{nombre_archivo}'.")
        return None


## Ejercicio N2: Analizar el DataFrame (Pandas)
def analizar_dataframe(df):
    """Muestra filas, columnas, tipos de datos, valores nulos y estadísticas descriptivas."""
    print("\n" + "="*60)
    print("ANÁLISIS DEL DATAFRAME", "\n", "="*60)
    print("Número de filas:", df.shape[0])
    print("Número de columnas:", df.shape[1])
    print("\nTipos de datos:")
    print(df.dtypes)
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    columnas_numericas = df.select_dtypes(include="number").columns.tolist()
    if columnas_numericas:
        print("\nEstadísticas descriptivas (columnas numéricas):")
        print(df[columnas_numericas].describe().round(2))
    else:
        print("\nNo hay columnas numéricas para describir.")
    return columnas_numericas


## Ejercicio N3: Análisis matemático (math)
def analisis_matematico(df, columnas_numericas):
    """Calcula raíz cuadrada, redondeos (ceil/floor) y logaritmo natural del valor máximo,
        ignorando columnas tipo ID (identificadores, no aportan valor estadístico)."""
    print("\n" + "="*60)
    print("ANÁLISIS MATEMÁTICO", "\n", "="*60)
    if not columnas_numericas:
        print("No hay columnas numéricas: se omite este análisis.")
        return
    columnas_utiles = [
        columna for columna in columnas_numericas
        if not search(r"\bid\b", columna.lower())
    ]
    if not columnas_utiles:
        columnas_utiles = columnas_numericas
    primera_columna = columnas_utiles[0]
    serie = df[primera_columna].dropna()
    promedio = serie.mean()
    maximo = serie.max()
    print(f"Columna numérica utilizada: '{primera_columna}'")
    print(f"Raíz cuadrada del promedio: {sqrt(promedio):.2f}")
    print(f"Prom. redondeado hacia arriba: {ceil(promedio)}")
    print(f"Prom. redondeado hacia abajo: {floor(promedio)}")
    if maximo > 0:
        print(f"Log. natural del valor máximo: {log(maximo):.2f}")
    else:
        print(f"El valor máximo ({maximo}) no es mayor que cero: no se calcula el logaritmo.")


## Ejercicio N4: Análisis de texto (re)
def analisis_texto(df):
    """Para las columnas de texto: cuenta registros con números, solo letras,
        caracteres especiales, y muestra las 5 palabras más frecuentes."""
    print("\n" + "="*60)
    print("ANÁLISIS DE TEXTO", "\n", "="*60)
    columnas_texto = df.select_dtypes(include=["object", "str"]).columns.tolist()

    if not columnas_texto:
        print("No hay columnas de tipo texto en el dataset.")
        return

    todas_las_palabras = []

    for columna in columnas_texto:
        print(f"\nColumna: '{columna}'")
        valores = df[columna].dropna().astype(str)

        con_numeros = valores.apply(lambda texto: bool(search(r"\d", texto))).sum()
        solo_letras = valores.apply(lambda texto: bool(match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", texto))).sum()
        con_especiales = valores.apply(lambda texto: bool(search(r"[^A-Za-z0-9ÁÉÍÓÚáéíóúÑñ\s]", texto))).sum()

        print(f"  Con números: {con_numeros}")
        print(f"  Solo letras: {solo_letras}")
        print(f"  Con caracteres especiales: {con_especiales}")

        for valor in valores:
            palabras = findall(r"[A-Za-zÁÉÍÓÚáéíóúÑñ]+", valor.lower())
            todas_las_palabras.extend(palabras)

    if todas_las_palabras:
        contador = Counter(todas_las_palabras)
        print("\n5 palabras más frecuentes (en todas las columnas de texto):")
        for palabra, frecuencia in contador.most_common(5):
            print(f"  {palabra}: {frecuencia}")


# --- Ejecución del programa ---
#1. Leer el archivo
df = leer_archivo(nombre_archivo)

if df is not None:
    print(f"\n REPORTE DE ANÁLISIS: {nombre_archivo}\n")

    #2. Analisis del DataFrame
    columnas_numericas = analizar_dataframe(df)
    #3. Analisis matemático
    analisis_matematico(df, columnas_numericas)
    #4. Analisis de texto
    analisis_texto(df)
    #5. Generación del reporte (cierre)
    print("\n" + "="*60)
    print("FIN DEL REPORTE")
    print("="*60)
else:
    print("Error: no se pudo leer el archivo")