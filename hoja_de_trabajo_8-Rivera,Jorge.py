"""
#Hoja de trabao 8-----------------------------------------------------
recorrido = int(input("Ingrese el tamaño de la lista: "))
multiplo = int(input("Ingrese el número para el cual desea los múltiplos: "))
list_x = []
for i in range(1, recorrido + 1):
    list_x.append(i * multiplo)
print(list_x)

#Ejercicio 2:
nombres = []
len_names = []
recorrido = int(input("Ingrese el tamaño de la lista: "))
for name in range(1, recorrido + 1):
    name = input("Ingrese un nombre: ")
    nombres.append(name)
    len_names.append(len(name))
print(nombres, "\n", len_names)
#Caso 1--------------------------------------------
En el restaurante de la universidad, el cliente luego de ser atendido evalúa la atención recibida
presionando un botón entre las 5 opciones mostradas.
Opciones:
5. Excelente
4. Muy Buena
3. Buena
2. Regular
1. Malo
Realice un algoritmo que registre en un arreglo la evaluación para n clientes atendidos, luego
deberá tabular las respuestas para mostrar:
a) Total de respuestas por tipo
b) La respuesta más frecuente
c) ¿Cuáles clientes respondieron con valores menores al promedio?
"""
excelente = 0
Muy_Buena = 0
buena = 0
regular =  0
malo = 0

persons = []
survey_result = []

total = 0
sur_mal = 0

recorrido = int(input("Cuántas personas van a votar: "))
for i in range(1, recorrido + 1):
    persons.append(i)
    encounter = input("Cómo calificaría la atención del restaurante 1.Malo, 2.Regular, 3.Buena, 4.Muy Buena, 5.Excelente: ")
    survey_result.append(encounter)
    match encounter:
        case "1":
            malo += 1
            total += 1
            sur_mal += 1
        case "2":
            regular += 1
            total += 2
            sur_mal += 1
        case "3":
            buena += 1
            total += 3
        case "4":
            Muy_Buena += 1
            total += 4
        case "5":
            excelente += 1
            total += 5
print("\n\nPromedio es igual a: {}".format(total / recorrido))
print("La respuesta más frecuente es: ", max(survey_result))
print("Los clientes que respondieron con valores menores al promedio son: ", "%",(sur_mal/recorrido)*100)
print(
    "\n\nExcelente: {}\nMuy Buena: {}\nBuena: {}\nRegular: {}\nMalo: {}".format(excelente, Muy_Buena, buena, regular, malo)
)
