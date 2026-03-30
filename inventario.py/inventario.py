#en esta lista se guardan todos los productos del inventario
inventario = []

#while true repite el menu hasta que el usuario elija salir
while True:
    print("MENU")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        #al marcar esta opcion se agregan los productos
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
#todos los productos se guardan como diccionario
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
#append agrega productos a la lista
        inventario.append(producto)
        print("Producto agregado correctamente")
    elif opcion == "2":
        #valida si no hay productos en el inventario 
        if len(inventario) == 0:
            print("El inventario esta vacio")
        else:
            for producto in inventario:
                print("Producto:", producto["nombre"],
                      "| Precio:", producto["precio"],
                      "| Cantidad:", producto["cantidad"])

    elif opcion == "3":
        total = 0
        cantidad_productos = 0

       #recorre el inventario y calcula el valor total y cantidades
        for producto in inventario:
            total = total + (producto["precio"] * producto["cantidad"])
            cantidad_productos = cantidad_productos + producto["cantidad"]

        print("Valor total del inventario:", total)
        print("Cantidad total de productos:", cantidad_productos)

    elif opcion == "4":
        print("Programa finalizado")
        #break se encarga de terminar el bucle cuando el usuario lo decida
        break

    else:
        print("Opción invalida, intente nuevamente")


#el objetivo de la semana fue aprender y utlizar listas y diccionarios en esenarios reales
#usar bucles y ciclos dentro de un programa real 
#agregar productos y calcular estadisticas de este invintario 
#