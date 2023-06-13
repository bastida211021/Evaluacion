"""7.	Construya un programa que genere una contraseña segura de longitud variable
 (por ejemplo, 10 caracteres) que contenga una combinación de letras mayúsculas,
   letras minúsculas, números y símbolos."""
"""para éste ejercicio, consideré lo siguiente
para las letras mayúsculas, los valores en ascii van del 65 al 90
para las letras minúsculas los valores en ascii van del 97 al 122
Para los números, los valores en ascii van del 48 al 57
Para los símbolos, los valores del ascii van del 33 al 47, del 58 al 64, del 91 al 96, del 123 al 126 """
import os #para poder usar el CLS y el PAUSE
import random #para generar la cadena
def evaluacontra(resultado):#funcion que evalua la contasena generada caracter por caracter
    indice=0 #para navegar entre la contrasena
    mayus=False #condición de mayúscula
    minus=False #condición de minúscula
    nums=False #condición de numeros
    symbols=False #condición de símbolos
    while indice<len(resultado): #ciclo principal de evaluación
        if ord(resultado[indice])>=65 and ord(resultado[indice])<=90: #si el caracter es una mayuscula
            mayus=True
        if ord(resultado[indice])>=97 and ord(resultado[indice])<=122: #si esl caracter es una minuscula
            minus=True
        if ord(resultado[indice])>=48 and ord(resultado[indice])<=57: #si el caracter es un numero
            nums=True
        if (ord(resultado[indice])>=33 and ord(resultado[indice])<=47)or(ord(resultado[indice])>=58 and ord(resultado[indice])<=64)or(ord(resultado[indice])>=91 and ord(resultado[indice])<=96) or (ord(resultado[indice])>=123 and ord(resultado[indice])<=126): #si el caracter es un símbolo
            symbols=True
        indice+=1
    if mayus and minus and nums and symbols: #si todas las condiciones se cumplieron
        return True #devuelve verdadero
    else: #si alguna no se cumplio
        return False #devuelve falso
def pidelongitud(): #función que pide la longitud de la contraseña
    print("Programa que genera contrasenas de al menos cuatro caracteres\nCon al menos una mayuscula, una minuscula, un simbolo y un numero\nIngrese la longitud de la contrasena")
    longitudcap=input()
    if int(longitudcap)<4:
        print("La longitud mínima es 4")
        return pidelongitud()
    else:
        return int(longitudcap)
def generacontra(longitud):#función que genera contraseñas caracter por caracter
    copialon=longitud #copia de la longitud
    contra=[]#para la contraseña generada
    while longitud>0: #ciclo que genera cada caracter de forma aleatoria entre numeros, letras y simbolos
        tipo=random.randint(1,7) #de forma aleatoria se determina que tipo de caracter va a ser
        if tipo==1:#para mayusculas
            contra.append(chr(random.randint(65,90)))
        if tipo==2:#para minusculas
            contra.append(chr(random.randint(97,122)))
        if tipo==3:#para numeros
            contra.append(chr(random.randint(48,57)))
        if tipo==4:#para simbolos
            contra.append(chr(random.randint(33,47)))
        if tipo==5:#para simbolos
            contra.append(chr(random.randint(58,64)))
        if tipo==6:#para simbolos
            contra.append(chr(random.randint(91,96)))
        if tipo==7:#para simbolos
            contra.append(chr(random.randint(123,126)))
        longitud-=1#restamos al contador
        resultado=''.join(contra) #convertimos la lista en cadena
    if evaluacontra(resultado):#si la contraseña generada se evalúa como valida
        return resultado #se regresa al programa principal
    else:#si no se consideró como valida, se hace recursiva hasta obtener una contraseña valida
        return generacontra(copialon)
while 1: #ciclo del programa principal
    print("La contrasena segura generada es: "+generacontra(pidelongitud()))#impresión de contraseña generada y validada
    os.system("pause") #pausa del sistema
    os.system("cls") #limpieza de pantalla
