notas1=float(input("ingrese la nota del parcial 1: "))
notas2=float(input("ingrese la nota del parcial 2: "))
notas3=float(input("ingrese la nota del parcial 3: "))
suma=notas1+notas2+notas3
print(f"el promedio de tus notas es: {suma/3}")

# Mostrar estudiantes
    elif opcion == "2":
        for estudiante in estudiantes:
            print(estudiante)

    # Buscar estudiante
    elif opcion == "3":
        buscar = input("Ingrese ID: ")

        for estudiante in estudiantes:
            if estudiante["id"] == buscar:
                print(estudiante)
