# Modulo N3
# Practica N3 
# Estudiante: Bredy Guerra

import sys
from math import sqrt
import pandas as pd
from re import match, search

"""
Instrucción: Usar el siquiente comando para llamar los datos en la consola:
python ventas.py ventas.csv
"""

#Usando sys, para obtener el nombre del archivo
nombre_archivo = sys.argv[1]
## Ejercicio N1: Cargar un dataset con Pandas
"""
Requisitos
** Importar sys.
** Obtener el nombre del archivo usando sys.argv.
** Leer el CSV utilizando pandas.
Mostrar:
    # # número de filas
    # # número de columnas
    # # nombres de las columnas
    # # primeras cinco filas
"""

def cargar_dataset(nombre_archivo):
    """Recibe el nombre del archivo de y devuelve el dataset."""
    df = pd.read_csv(nombre_archivo)
    return df

def mostrar_informacion(df):
    """Muestra número de filas, columnas, nombres de columnas y primeras 5 filas."""
    print("Ejercicio N1: Cargar un Dataset con Pandas", "\n")
    print("Número de filas:", df.shape[0])
    print("Número de columnas:", df.shape[1])
    print("Nombres de columnas:", list(df.columns))
    print("Primeras cinco filas:")
    print(df.head(5))
    print("\n", "="*60)

## Ejercicio 2. Estadísticas utilizando Math
"""
A partir del dataset:
Calcular:
    # # Total de ventas.
    # # Promedio del precio.
    # # Raíz cuadrada del total vendido.
    # # Precio máximo.
    # # Precio mínimo.
Librerías utilizadas
pandas
math
"""
def calcular_estadisticas(df):
    """Calcula total de ventas, promedio, raíz cuadrada del total, precio máximo y mínimo."""
    total_ventas = (df["Cantidad"] * df["Precio"]).sum()
    promedio_precio = df["Precio"].mean() 
    raiz_total = sqrt(total_ventas)
    precio_max = df["Precio"].max()
    precio_min = df["Precio"].min()

    print("Ejercicio N2: Estadísticas utilizando Math", "\n")
    print("Total de ventas:", total_ventas)
    print("Promedio del precio:", promedio_precio)
    print("Raíz cuadrada del total vendido:", raiz_total)
    print("Precio máximo:", precio_max)
    print("Precio mínimo:", precio_min)
    print("\n", "="*60)

## Ejercicio 3. Validación de correos electrónicos
"""
Utilizando la columna Email, validar cuáles tienen un formato correcto
mediante expresiones regulares.
    # # Utilizar una expresión similar a: ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
    # # Agregar una nueva columna llamada Email_Valido con los valores Sí / No
Librerías utilizadas
pandas
re
"""
def validar_emails(df):
    """Valida el formato de cada email con re y agrega la columna Email_Valido."""
    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    df["Email_Valido"] = df["Email"].apply(
        lambda correo: "Sí" if match(patron, correo) else "No"
    )

    print("Ejercicio N3: Validación de correos electrónicos", "\n") 
    print(df[["Email", "Email_Valido"]]) # Mostrar los correos electrónicos con su validación
    print("\n", "="*60)

## Ejercicio 4. Buscar dominios de correo
"""
Extraer únicamente el dominio del correo electrónico.
Ejemplo : juan@gmail.com
Resultado: gmail.com
Crear una nueva columna
    Dominio
Al finalizar mostrar cuántos usuarios utilizan cada dominio.
Ejemplo
    # gmail.com      10
    # hotmail.com     3
    # yahoo.com       2

Librerías utilizadas: pandas, re
"""
def extraer_dominios(df):
    """Extrae el dominio de cada email con regex y agrega la columna Dominio."""
    patron_dominio = r"@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$"

    def obtener_dominio(extension_correo):
        resultado = search(patron_dominio, str(extension_correo))
        return resultado.group(1) if resultado else "Desconocido"

    df["Dominio"] = df["Email"].apply(obtener_dominio)

    print("Ejercicio N4: Dominios de correo", "\n")
    print(df[["Email", "Dominio"]])
    print("\nUsuarios por dominio:")
    print(df["Dominio"].value_counts())

    print("\n", "="*60)

## Ejercicio 5. Generar una nueva columna
"""
Crear una columna Total donde Total = Cantidad × Precio
Posteriormente mostrar:
    # # venta más alta
    # # venta más baja
    # # promedio de ventas
"""
def calcular_total(df):
    """Crea la columna Total (Cantidad x Precio) y muestra venta más alta, más baja y promedio."""

    df["Total"] = df["Cantidad"] * df["Precio"]

    venta_mas_alta = df["Total"].max()
    venta_mas_baja = df["Total"].min()
    promedio_ventas = df["Total"].mean()

    print("Ejercicio N5: Columna Total", "\n")
    print(df[["Cliente", "Producto", "Cantidad", "Precio", "Total"]])
    print("\nVenta más alta:", venta_mas_alta)
    print("Venta más baja:", venta_mas_baja)
    print("Promedio de ventas:", promedio_ventas)
    print("\n", "="*60)

# --- Númeració de ejecución del programa ---
#1.     Leer el archivo
df = cargar_dataset(nombre_archivo)
#2.     Ejercicio 1. Cargar un dataset con Pandas
mostrar_informacion(df)
#3.     Ejercicio 2. Estadísticas utilizando Math
calcular_estadisticas(df)
#4.     Ejercicio 3. Validación de correos electrónicos
validar_emails(df)
#5.     Ejercicio 4. Buscar dominios de correo
extraer_dominios(df)
#6.     Ejercicio 5. Generar una nueva columna
calcular_total(df)