#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por
#pantalla otro correo electrónico con el mismo nombre (la parte delantera de la arroba @) pero
#con dominio ceu.es.

correo = input("Introduce un correo: ")
correo_nuevo = correo[:correo.find("@")] + "@ceu.es"

print(correo_nuevo)