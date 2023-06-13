"""5.	Establezca una función que genere la secuencia de Fibonacci. La secuencia inicia con 0,1, después se itera el numero de veces que ingreso """
import os #para poder usar la limpieza de la terminal
os.system("cls") #limpiar terminal
def fibonacci(iteraciones):#definición de la función
    lista=[0,1] #lista donde se guarda la serie
    j=0 #contador
    while(j<iteraciones): #se itera hasta el numero ingresado
        lista.append(lista[(len(lista)-1)]+lista[(len(lista)-2)])#se accede a la lista en cada iteración para obtener los dos últimos elementos de la serie
        j+=1 #aumento de contador
    print(lista) #se imprime la lista
print("Este programa genera la secuencia de fibonacci, por favor ingrese el numero de iteraciones")
iteraciones=input()#solicitamos el numero de iteraciones
fibonacci(int(iteraciones))#llamada de función