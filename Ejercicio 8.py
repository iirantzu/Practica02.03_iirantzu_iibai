#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("Introduce el precio con dos decimales: ")

entero = precio[:precio.find(".")]
decimal = precio[precio.find(".")+1]
decimal2 = precio[precio.find(".")+2]
print("El precio total es: " + entero + " euros con " + decimal + decimal2 + " centimos")