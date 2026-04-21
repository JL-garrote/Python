import csv
import json

cocheCaro = 0

def sacarCocheCaro() :
    precioMax = 0
    media = []

    with open("Coches.csv" , "r",encoding="utf-8") as fichero:
        lectorCSV = csv.reader(fichero)
        next(lectorCSV)

        for fila in lectorCSV:
            precio = int(fila[4])
            media.append(precio)

            if(precio > precioMax) :
               precioMax = precio
            
    suma = sum(media) / len(media)

    print(f"la media es de {suma}")
    return precioMax

def leerJSON() :
    with open("alumnos.json","r",encoding="utf-8") as j:
        contenido = json.load(j)

        for alumno in contenido:
            notas = alumno["notas"]
            media = sum(notas.values()) / len(notas)

    return media

cocheCaro = sacarCocheCaro()
mediaAcademica = leerJSON()

if(mediaAcademica >= 4.99) :
    print(f"Has aprobado tienes derecho a reclamar un coche de {cocheCaro}")
else :
    print(f"Has suspendido con una media de {mediaAcademica}")