"""6.	Componga un código de un juego en el que la computadora genera un número aleatorio
 y el jugador debe adivinarlo en un número máximo de intentos. La computadora debe 
 proporcionar retroalimentación diciendo si el número ingresado es mayor o menor 
 que el número objetivo."""
import os #para poder usar el cls
import random #para poder generar el numero aleatorio
os.system("cls") #limpieza de la terminal
def adivinaelnum():#definición de la función principal
    os.system("cls") #limpieza de pantalla
    objetivo=random.randint(0,100) #generación del numero aleatorio entre cero y 100
    intentos=10 #numero máximo de intentos
    while intentos>0: #ciclo para restar intentos
        print("ADIVINA EL NUMERO, por favor, ingresa un numero "+str(objetivo))
        numero=int(input()) #solicitud del numero al usuario
        if numero<objetivo:#comparativa si es menor
            os.system("cls")#limpieza de la terminal
            print("El numero "+str(numero)+" es menor al objetivo") #retroalimentación
        elif numero>objetivo: #comparativa de mayor que
            os.system("cls")#limpieza de la terminal
            print("El numero "+str(numero)+" es mayor al objetivo") #retroalimentación
        else:
            return True #retorno de la función si es el mimso numero
        print("te quedan "+str(intentos-1)+" intentos") #muestra de los intentos restantes
        intentos-=1 #quitamos un intento
    return False #retorno de que perdió el juego
    
while 1: #ciclo principal del programa
    if adivinaelnum(): #si ganó el juego
        os.system("cls")#limpieza de la terminal
        print("Felicidades, adivinaste el numero") #mensaje de ganador
    else: #si no ganó
        os.system("cls")#limpieza de la terminal
        print("\nPerdiste!") #mensaje de perdedor
    os.system("pause") #pausa del sistema para reinciar el jeugo