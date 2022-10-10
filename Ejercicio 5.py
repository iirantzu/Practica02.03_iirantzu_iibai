#Escribir un programa que pida al usuario que introduzca una frase
#en la consola y muestre por pantalla la frase invertida.

texto = input("Introduce una frase: ")

print(texto[::-1])
spl = texto.split(" ")
print(spl[::-1])