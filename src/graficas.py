import matplotlib.pyplot as plt


def grafica_temperatura():
    print("=== Gráfica Temperatura vs Tiempo ===")
    tiempo = [1, 4, 6, 8, 10, 12]
    temperatura = [20, 23, 27, 25, 23, 19]

    plt.plot(tiempo, temperatura)
    plt.xlabel("Tiempo (hrs)")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperatura vs Tiempo")
    plt.grid(True)
    plt.show()


def grafica_promedios_materias():
    print("=== Gráfica de promedios por materia ===")
    materias = ["Programación", "Física", "Geometría", "Cálculo"]
    promedios = [66, 55, 78, 92]

    plt.bar(materias, promedios)
    plt.ylabel("Promedio")
    plt.title("Promedio por materia")
    plt.show()


if __name__ == "__main__":
    grafica_temperatura()
    grafica_promedios_materias()
