import csv
import json

with open("fichero.txt" ,"r") as f:
    for linea in f:
        print(linea)


with open("Coches.csv","r",encoding="utf-8") as f:
    linea = csv.reader(f)
    for linea in f:
        print(f"Leyendo CSV {linea}")


with open("alumnos.json","r",encoding="utf-8") as f:
    lector = json.load(f)
    print(f"Leyendo JSON {lector}")