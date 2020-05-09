#Imports de excel
import csv
with open("lista_container_enviado.csv") as file:
    reader = list(csv.DictReader(file, delimiter=";"))

for linea in reader:
    print(linea)



with open("info_barcos.csv") as file:
    reader = list(csv.DictReader(file, delimiter=";"))

for linea in reader:
    print(linea)
