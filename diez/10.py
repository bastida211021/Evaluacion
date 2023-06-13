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
import json
ruta="diez/response.json"
def cargardatos(ruta):
    with open(ruta) as contenido:
        cursos=json.load(contenido)
    #print(cursos)
    contenido.close()
    return cursos
def analiza_tipos_de_dato(contenidoarchivo):
    listatipodedato=[]
    for elemento in contenidoarchivo:
        listatipodedato.append(type(contenidoarchivo[elemento]))
    print(listatipodedato)

contenidoarchivo=cargardatos(ruta)
analiza_tipos_de_dato(contenidoarchivo)