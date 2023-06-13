"""4.	Componga un programa que implemente el juego del ahorcado. El juego consiste en adivinar una palabra oculta, letra por letra, antes de que se complete un dibujo del ahorcado. El programa debe tener las siguientes características:
•	Elija una palabra al azar de una lista predefinida de palabras.
•	Muestre un espacio en blanco por cada letra de la palabra oculta.
•	Permita al jugador ingresar una letra adivinada.
•	Verifique si la letra adivinada se encuentra en la palabra oculta.
•	Si la letra adivinada está en la palabra, muestre la posición(es) de la letra en la palabra.
•	Si la letra adivinada no está en la palabra, muestre un mensaje indicando que la letra es incorrecta y dibuja una parte del ahorcado.
•	Continúe solicitando al jugador que ingrese letras hasta que adivine la palabra completa o se complete el dibujo del ahorcado.
•	Muestre un mensaje de victoria si el jugador adivina la palabra completa antes de completar el dibujo del ahorcado, o muestra un mensaje de derrota si se completa el dibujo antes de adivinar la palabra.
"""
import random #librería para el uso de funciones rand
import os #para poder usar el pause y el cls
#creación de la parte gráfica del ahorcado, imagen por imagen
ahorcado = ['''
  +---+
  |   |
      |
      |
      |
      |
========= Error 1 de 6''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= Error 2 de 6''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= Error 3 de 6''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= Error 4 de 6''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= Error 5 de 6''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= Error 6 de 6''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= Perdiste!''']
#creación de la lista de palabras
palabras=["Cirujano","Evadir","As","Liquido","Mentir","Cadera","Astronauta","Zafiro","Nido","Abrelatas"]
#función principal del juego del ahorcado
def iniciajuego():
    print("\n\nBienvenido al juego de ahorcado, tienes 6 oportunidades antes de perder\n")
    secreta=palabras[random.randint(0,len(palabras)-1)].lower()#obtención de la palabra secreta
    print(ahorcado[0])
    copia="_"*len(secreta)#creación de cadena con los espacios en blanco
    print(copia)
    intentos=0
    while intentos<len(ahorcado)-1:#ciclo principal del juego
        print("Introduce una letra:")
        letra=input()#solicitamos la letra al usuario
        os.system("cls")#limpieza de pantalla
        coincidencias = [i for i, c in enumerate(secreta) if c == letra]#enlistamos las posiciones en las que encontramos la letra que el usuario tecleó
        if len(coincidencias)==0:#si no hubo coincidencias
            print("\n\nLetra equivocada")
            intentos+=1
        else:
            print("\n\nLetra encontrada") #si hubo coincidencias
            respaldo=""#cadena vacía para agregar los caracteres ya encontrados,con los nuevos
            for elemento in coincidencias:#ciclo con las posiciones en coincidencias
                j=0 #contador para el total de caracteres
                while j<len(secreta):#mientras el contador sea menor a los caracteres de la palabra
                    if j==elemento:#si el contador llega a la posición donde debería ir el caracter
                        respaldo+=secreta[j]#actualiza el caracter tomado de la palabra secreta
                    else:
                        respaldo+=copia[j]#actualiza el caracter tomado de la cadena de espacios
                    j+=1 #aumento del contador
                copia=respaldo #actualización de la cadena copia
                respaldo="" #vaciamos la cadena de nuevo
        if copia==secreta:#si la palabra generada ya es igual a la secreta
            print("\n\n\nFelicidades, ganaste") #mensaje de victoria
            break #salida del ciclo
        print(copia) #imprimimos la cadena final generada
        print(ahorcado[intentos]) #imprimimos el resultado gráfico del ahorcado
    print("La palabra secreta: "+secreta)
    print("Juego terminado\n\n")#mensaje del fin del juego
    os.system("pause") #en espera de respuesta en teclado
    os.system("cls") #limpieza de pantalla
while 1: #ciclo que obliga al juego a reiniciarse al ganar o perder
    iniciajuego()#llamada de la función principal