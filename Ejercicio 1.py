#Escribir un programa que pregunte el nombre del usuario
#en la consola y un número entero e imprima por pantalla
#en líneas distintas el nombre del usuario tantas veces
#como el número introducido.

nombre = input("Introduce tu nombre:\n")
num_copias = int(input("¿Cuantas veces quieres repetirlo?:\n"))

print((nombre + "\n") * num_copias )