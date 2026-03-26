#indica al ususario que ingrese el nombre del producto
nombre=input("ingrese el nombre del producto: ")
while True: 
    try:
        #indica al usuario ingresar el valor del producto
        precio=float(input("ingrese el precio del producto: "))
        break
    except ValueError:
        print("por favor ingrese un numero valido para el precio.")
while True: 
    try:
        #indica al usuario que debe ingresar la cantidad
        cantidad=int(input("ingrese la cantidad del producto: ")) 
        break
    except ValueError:
        print("por favor ingrese una cantidad valida del producto.") 
        #multiplica el valor total y muestra el total en pantalla
costo_total=(precio*cantidad)        
print("datos registrados: ")  
print(f"producto: {nombre}")
print(f"precio: {precio}")
print(f"cantidad: {cantidad}")       
print(f"total: {costo_total}")
print(f"producto: {nombre} / precio: {precio} / cantidad: {cantidad} / total: {costo_total}")

#el programa registra un producto y valida los datos ingresados 
#calcula los datos y muestra el resultado en pantalla