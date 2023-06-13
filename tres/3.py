"""3.	Haga un programa que recorra una carpeta y sus subcarpetas,
y encuentre archivos duplicados basándose en el contenido de los archivos.
Muestra una lista de los archivos duplicados encontrados."""
import os #para poder usar el acceso del SO
import filecmp #para poder usar el comparador de archivos
ubicacion="tres\Carpeta"#ruta en la que se encuentra la carpeta principal
listadearchivos=[]#lista donde se guardan todas las rutas con los archivos encontrados

def explora(ubicacion):#función iterativa que explora la ruta en busca de todas las subcarpetas y sus archivos
    lista=os.listdir(ubicacion)#enlistamos todo lo que hay dentro de la carpeta
    for ubi in lista:#bucle que abre las ubicaciones desglosadas para buscar más archivos
        ubi=ubicacion+"\\"+ubi #edición de la lista con la ruta completa
        if os.path.isdir(ubi):#si la ubicación actual es un directorio
            explora(ubi) #recursiva que busca más subcarpetas
        if os.path.isfile(ubi):#si la ubicación actual es un archivo
            listadearchivos.append(ubi)#se agrega el archivo a la lista de archivos


explora(ubicacion)#llamada de la función con la ruta principal
print("\n\nA partir de la ubicacion: "+ubicacion+" se encontraron los siguientes archivos:\n")
for elemento in listadearchivos:
    print(str(listadearchivos.index(elemento)+1)+") "+elemento)
print("\n\n A continuacion se muestran los archivos duplicados en contenido:")
actual=0#para navegar entre la lista de archivos encontrados
fin=len(listadearchivos)#determinamos la cantidad de archivos encontrados
while actual<fin:
    siguiente=actual+1
    while siguiente<fin:
        if filecmp.cmp(listadearchivos[actual], listadearchivos[siguiente], shallow=False):
            print(""+listadearchivos[actual]+" esta duplicado en: "+listadearchivos[siguiente])
        siguiente+=1
    actual+=1