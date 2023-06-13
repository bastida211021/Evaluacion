"""9.	Desarrolle una función que devuelva la longitud de una polilínea 
cualquiera que se le pase a la función con la siguiente estructura
 [[x1, y1], [x2, y2], [x3, y3], [x4,y4]…..[xn, yn]]"""
import random #para generar los puntos de forma aleatoria
import os
import math
def generapuntosaleatorios(): #esta función genera una lista con puntos en el plano cartesiano
    puntos=random.randint(2,15) #numero de puntos, el minimo es dos
    lista=[]#lista vacía a la que se le agregarán los puntos
    contador=0#contador para agregar los puntos a la lista
    while contador<puntos:
        lista.append([random.randint(-10,10),random.randint(-10,10)])
        contador+=1
    return lista
def calculalongitud(lista):#función solicitada
    print("La polilinea dada por los puntos: "+str(lista))#impresión de los puntos de la linea
    puntos=len(lista)#obtención de la cantidad de puntos
    contador=0 #para navegar en la lista
    longitud=0.0 #sumador de longitud
    while contador<(puntos-1):#ciclo principal
        longitud+=math.sqrt((lista[contador+1][0]-lista[contador][0])**2+(lista[contador+1][1]-lista[contador][1])**2)#descomposición de dos puntos de la linea
        contador+=1 #aumento de contador
    return longitud #retorno de la longitud

while 1: #ciclo del programa principal
    os.system("cls") #limpieza de pantalla
    print("Tiene longitud de:"+str(calculalongitud(generapuntosaleatorios()))) #llamada de función
    os.system("pause")#pausa antes de generar otra línea