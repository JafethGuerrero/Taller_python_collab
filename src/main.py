
from funciones import (
    imprimir_nombre_completo,
    contar_pares_y_convertir,
)
import io_basico
import estructuras_control
import analisis_datos
import graficas


def opcion_1_io_basico():
    print("\n=== Opción 1: Entrada / salida básica ===")
    # Demostración con datos fijos
    imprimir_nombre_completo("Jafeth", "Guerrero Serrano", "ISC")
    io_basico.saludo_basico()
    # Demostración interactiva
    io_basico.captura_datos_persona()


def opcion_2_estructuras_control():
    print("\n=== Opción 2: Estructuras de control (if / for / while) ===")
    estructuras_control.calculadora()
    estructuras_control.ciclos_for_while()


def opcion_3_listas_promedio():
    print("\n=== Opción 3: Listas y promedio de calificaciones ===")
    estructuras_control.promedio_lista()


def opcion_4_pares_impares():
    print("\n=== Opción 4: Actividad pares / impares (15 números) ===")
    numeros = []
    for i in range(15):
        n = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(n)

    cantidad_pares, lista_convertida = contar_pares_y_convertir(numeros)
    print("\nNúmeros ingresados:", numeros)
    print("Cantidad de pares:", cantidad_pares)
    print("Lista con impares convertidos a pares:", lista_convertida)


def opcion_5_analisis_datos():
    print("\n=== Opción 5: Análisis de datos con pandas / numpy ===")
    analisis_datos.cargar_y_mostrar()
    analisis_datos.calcular_promedio_y_estatus()


def opcion_6_graficas():
    print("\n=== Opción 6: Gráficas con matplotlib ===")
    graficas.grafica_temperatura()
    graficas.grafica_promedios_materias()


def main():
    while True:
        print("\n==============================")
        print("  Taller Python - Menú principal")
        print("==============================")
        print("1) Entrada / salida básica")
        print("2) Estructuras de control (if / for / while)")
        print("3) Listas y promedio de calificaciones")
        print("4) Actividad pares / impares (15 números)")
        print("5) Análisis de datos con pandas / numpy")
        print("6) Gráficas con matplotlib")
        print("7) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            opcion_1_io_basico()
        elif opcion == "2":
            opcion_2_estructuras_control()
        elif opcion == "3":
            opcion_3_listas_promedio()
        elif opcion == "4":
            opcion_4_pares_impares()
        elif opcion == "5":
            opcion_5_analisis_datos()
        elif opcion == "6":
            opcion_6_graficas()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
