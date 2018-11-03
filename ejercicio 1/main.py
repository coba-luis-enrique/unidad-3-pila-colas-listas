from operacion import *

print("ACTIVIDAD UNO.-UNA LISTA QUE LLENA UNA LISTA CON CARACTERES Y LOS IMPRIMA DE MANERA INVERSA")
#usar una sola lista

print("presione 1 para finalizar")
print("ingrese un caracter:")
n=input()

pila=pila(n)
pila.apilar()
print("los datos se han traspasado")
print("lista inversa :", *pila.desapilar())

