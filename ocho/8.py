"""8.	Desarrolle una calculadora de fechas que permita al usuario realizar operaciones
 como sumar o restar días, meses o años a una fecha dada. El programa debe manejar 
 adecuadamente los casos de cambio de mes o año."""
from datetime import datetime #librería para el manejo de fechas
#from datetime import timedelta #para poder usar el delta en fechas
from dateutil.relativedelta import relativedelta #para poder usar el delta en  dias,meses,y años
import os
def realizaoperacion(fechaingresada):
    print("Qué operación desea hacer con la fecha ingresada?\n1) sumar días, meses y años\n2) restar días, meses y años")
    respuesta=int(input())
    os.system("cls")
    if respuesta==1:
        print("Se sumarán años, meses, días y horas a la fecha "+str(fechaingresada.strftime("%d/%m/%Y")))
        print("La fecha calculada es: "+str((fechaingresada+pidelta()).strftime("%d/%m/%Y")))
    elif respuesta==2:
        print("Se restarán años, meses, días y horas a la fecha "+str(fechaingresada.strftime("%d/%m/%Y")))
        print("La fecha calculada es: "+str((fechaingresada-pidelta()).strftime("%d/%m/%Y")))
    
def pidelta():#función que solicita la candidad de días, meses y años a sumar o restar
    print("Ingrese la cantidad de dias")
    dias=int(input())
    print("Ingrese la cantidad de meses")
    meses=int(input())
    print("Ingrese la cantidad de anos")
    anos=int(input())
    return relativedelta(days=dias,months=meses,years=anos)#creación del objeto relative delta
def pidefecha(): #función que pide la fecha al usuario
    os.system("cls")
    print("Calculadora de fechas\nIngrese una fecha en formato dd/mm/yyyy")
    fecha=input()
    try:
         fechaingresada=datetime.strptime(fecha,'%d/%m/%Y')
    except ValueError:
         print("El formato no es el especificado dos numeros para el dia/dos numeros para el mes/cuatro numeros para el año)")
         os.system("pause")
         return pidefecha()#recursiva para volver a intentarlo
    return fechaingresada

while 1:
    realizaoperacion(pidefecha())
    os.system("pause")
