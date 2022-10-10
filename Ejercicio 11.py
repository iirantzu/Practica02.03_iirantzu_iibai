#Escribir un programa que pregunte el nombre el un producto, su precio y un número de
#unidades y muestre por pantalla una cadena con el nombre del producto seguido de su
#precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres
#dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = input("Producto:\n")
precio = float(input("Precio:\n"))
unidades = int(input("Unidades:\n"))
cadena = "{producto}: {precio:6.2f}€ * {unidades:3d} = {total:8.2f}€"

print(cadena.format(producto=producto, precio=precio, unidades=unidades, total=precio*unidades))