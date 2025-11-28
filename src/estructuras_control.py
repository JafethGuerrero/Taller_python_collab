def calculadora():
    x = int(input("Primer valor: "))
    y = int(input("Segundo valor: "))

    print("¿Qué operación deseas? : ")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")

    operacion = int(input("Opción: "))

    if operacion == 1:
        print(f"La respuesta es: {x + y}")
    elif operacion == 2:
        print(f"La respuesta es: {x - y}")
    elif operacion == 3:
        print(f"La respuesta es: {x * y}")
    else:
        print(f"La respuesta es: {x / y}")


def ciclos_for_while():
    print("=== For sencillo 0 a 9 ===")
    for i in range(10):
        print(i)

    print("\n=== For con inicio, fin y paso (1 a 10 de 3 en 3) ===")
    for i in range(1, 11, 3):
        print(i)

    print("\n=== While de 0 a 4 ===")
    cont = 0
    while cont < 5:
        print(f"El valor es: {cont}")
        cont += 1


def promedio_lista():
    print("=== Promedio de calificaciones con for ===")
    calif = [4, 6, 9, 7, 5]

    suma = 0
    for i in range(len(calif)):
        suma += calif[i]

    prom = suma / len(calif)
    print("Calificaciones:", calif)
    print("Promedio:", prom)


if __name__ == "__main__":
    calculadora()
    ciclos_for_while()
    promedio_lista()
