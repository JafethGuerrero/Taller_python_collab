def saludo_basico():
    print("Hola   mundo")

    nombre = "Jafeth"
    carrera = "ISC"
    print(f"{nombre} es de la carrera de {carrera}")


def captura_datos_persona():
    print("=== Captura de datos de una persona ===")
    nombre = input("¿Cómo te llamas? ")
    edad = int(input("Tu edad: "))
    estatura = float(input("Tu estatura en cm: "))

    print(f"Hola {nombre}, tienes {edad} años y mides {estatura} cm.")


if __name__ == "__main__":
    # Pequeña demo si ejecutas este archivo directo
    saludo_basico()
    captura_datos_persona()
