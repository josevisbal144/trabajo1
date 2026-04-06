nota1=float(input("ingrese la nota del parcial 1: "))
nota2=float(input("ingrese la nota del parcial 2: "))
nota3=float(input("ingrese la nota del parcial 3: "))
notas=[nota1, nota2, nota3]
promedio = sum(notas) / len(notas)
print(promedio)

# Actualizar notes
    elif opcion == "4":
        buscar = input("Ingrese ID: ")

        for notes in notes:
            if notes["id"] == buscar:
                notes["nombre"] = input("Nuevo nombre: ")
                notes["edad"] = int(input("Nueva edad: "))

    # Eliminar notes
    elif opcion == "5":
        buscar = input("Ingrese ID: ")

        for notes in notes:
            if notes["id"] == buscar:
                notes.remove(notes)

    # Salir
    elif opcion == "6":
        print("Programa finalizado")

    else:
        print("Opción incorrecta")
