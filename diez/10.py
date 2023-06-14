"""10.	Basado en la estructura del json (response.json) anexo,
crear un código que valide que los tipos de datos contenidos en
cada parámetro sean los que están definidos de forma correcta en dicho
json de tal forma que en caso de modificar el archivo y reemplazar algún tipo de
dato, el código lo detecte y mande el mensaje de error indicando la posición y 
el parámetro en el que se esté encontrando el conflicto. 
Ejemplo: “route_name”: 20.5  ----- > el parámetro ahora se manda como entero en 
lugar de como cadena de texto como originalmente estaba en el json, por lo que el
mensaje de error indicaría algo como “El route_name debe ser string no int”
Para el caso de parámetros que estén dentro de listas de objetos, indicar la posición 
del objeto en donde se encuentre el parámetro conflictivo. Suponiendo que se encuentre
en el segundo objeto de la lista de “sectors” indicar el parámetro que no cumple con 
el tipo de dato adecuado  e indicar además la posición del objeto en dicha lista.
Recomendación. Hacer uso de Excepciones.
"""
import json #para poder importar el json como diccionario
rutaoriginal="diez/response.json"#ubicación del json original
rutasecundario="diez/response2.json"#ubicacion del json secundario

def cargarchivo(ruta):#función para importar el json, recibe la ubicación del archivo, retorna el diccionario importado
    with open(ruta) as contenido:
        cursos=json.load(contenido)
    contenido.close()
    return cursos

def compararchivos(jsonoriginal,jsonsecundario,ubi=""):#función para comparar los archivos json
    #en caso de recibir una variable
    try:
        if type(jsonoriginal)!=type(jsonsecundario):
            raise TypeError
    except TypeError:
            print(("El campo: "+ubi+" debe ser "+str(type(jsonoriginal))+" no "+str(type(jsonsecundario))))
    #en caso de recibir una lista
    if (type(jsonoriginal)== list):
        for index, item1 in enumerate(jsonoriginal):
            ubirelativa = f"{ubi}[{index}]"
            item2 = jsonsecundario[index]
            compararchivos(item1, item2,ubirelativa)
    #en caso de recibir un diccionario
    if(type(jsonoriginal)== dict):
        for key in jsonoriginal:
            ubirelativa= ubi + '/' + key if ubi else key
            compararchivos(jsonoriginal[key], jsonsecundario[key],ubirelativa)
jsonoriginal=cargarchivo(rutaoriginal)#carga del archivo base
jsonsecundario=cargarchivo(rutasecundario)#carga del archivo a comparar
compararchivos(jsonoriginal,jsonsecundario,"")