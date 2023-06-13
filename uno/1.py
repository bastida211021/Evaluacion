"""
1.	Realice un programa que cuente la cantidad de palabras en un archivo de texto.
El programa debe solicitar al usuario el nombre del archivo y mostrar el número total
de palabras como respuesta en la terminal de ejecución.
"""
print("Programa para contar las palabras de un archivo de texto, \nIngrese el nombre del archivo:")
file=input()
file="uno\\"+file
print("\nIntentando abrir el archivo "+file)
import os #para asegurarse que el archivo existe
if os.path.exists(file):#si el archivo existe
    print("\nArchivo encontrado\n")
    archivo=open(file,"r")#abre el archivo
    cadena=archivo.read()#lee el archivo
    if cadena=="":#si el archivo está vacio
        print ("\nArchivo vacio")
    else:#si el archivo no está vacío
        """Para la resolución de éste ejercicio propongo dos soluciones,
        la primera contando los espacios y los saltos de línea usando el método count() de string, es rápido y
        se requiere poco código, sin embargo el resultado dependerá enteramente de la calidad de redacción del archivo
        """
        print ("Usando el primer metodo, el archivo\n")
        print(cadena)
        print ("\nTiene "+str(cadena.count(' ')+cadena.count('\n')+1)+" palabras")
        """
        Para la segunda solución, propongo un barrido completo del archivo,
        que tiene como condición aumentar el contador si y solo si, el caracter en cuestion preede de un salto de línea o
        un espacio en blanco, más la palabra de inicio que carece de caracter en blanco, o salto de linea
        """
        counter=1 #para el contador de palabras, inicia en uno considerando que el texto inicia con palabra, no con espacio o salto de linea
        anterior='%'#inicializamos el comparador
        for actual in cadena:
            if ((anterior=='\n' or anterior==' ')and ((actual!='\n')and(actual!=' '))):
                counter+=1
            anterior=actual
        print("\nUsando el segundo metodo se contaron "+str(counter)+" palabras")
        archivo.close #cerramos el archivo
else:
    print("\nEl archivo no existe")
