import pandas as pd
import numpy as np


def cargar_y_mostrar():
    print("=== Lectura de archivo datos.xlsx ===")
    df = pd.read_excel("data/datos.xlsx")
    print(df.head())
    print("\nDescripción rápida:")
    print(df.describe())


def calcular_promedio_y_estatus():
    print("=== Cálculo de promedio y estatus ===")
    df = pd.read_excel("data/datos.xlsx")

    df["prom"] = df[["Parcial 1", "Parcial 2", "Parcial 3"]].mean(axis=1)
    df["estatus"] = np.where(df["prom"] >= 7, "Aprobado", "Reprobado")

    print(df)

    df.to_excel("data/datos_mod.xlsx", index=False)
    print("\nArchivo guardado como data/datos_mod.xlsx")


if __name__ == "__main__":
    cargar_y_mostrar()
    calcular_promedio_y_estatus()
