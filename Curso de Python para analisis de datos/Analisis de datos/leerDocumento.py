import csv
import json

with open("Curso de Python para analisis de datos\\Analisis de datos\\fichero.txt" ,"r") as f:
    for linea in f:
        print(linea)


with open("Curso de Python para analisis de datos\\Analisis de datos\\Coches.csv","r",encoding="utf-8") as f:
    linea = csv.reader(f)
    for linea in f:
        print(f"Leyendo CSV {linea}")


with open("Curso de Python para analisis de datos\\Analisis de datos\\alumnos.json","r",encoding="utf-8") as f:
    lector = json.load(f)
    print(f"Leyendo JSON {lector}")