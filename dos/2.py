"""2.	Escriba una función que verifique si una palabra o frase ingresada por el usuario es un palíndromo."""
"""Para la solución de éste ejercicio, consideré que un palíndromo puede consistir en una palabra o una frase
la frase puede contener mayúsculas, minúsculas, y caracteres especiales"""
def espalindromo(cadena):#definición de la función
    nueva_cadena = ''.join(char for char in cadena if char.isalnum())#Esta linea une en una nueva cadena, los caracteres si y solo si son alfanuméricos
    nueva_cadena=nueva_cadena.lower()#Esta linea convierte todos los caracteres a minusculas
    inicio = 0 #inicializamos el inicio del bucle
    fin = len(nueva_cadena) - 1 #Tomamos el fin del bucle
    while nueva_cadena[inicio] == nueva_cadena[fin]:#bucle principal, mientras los caracteres sean iguales
        if inicio >= fin: #es suficiente con analizar la mitad de la cadena para determinar si es o no es palindromo
            return True #devuelve verdadero si es palíndromo
        inicio += 1 #aumento de los contadores
        fin -= 1
    return False #devuelve falso si hay caracteres diferentes
print("Ingrese la palabra o frase para determinar si es palindromo\n")
cadena=input()
print ("La palabra o frase: "+cadena)
if espalindromo(cadena):
    print ("Es palindromo")
else:
    print ("No es palindromo")