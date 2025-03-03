#fecha
numero = int(input("Ingrese el año ddmmaaaa: "))
year = numero % 10000
month = (numero // 10000) % 100
day = (numero // 1000000)
#cálculo de bisiesto
bisis = False
biyear = year % 4
if biyear == 0:
    bisis = True
    print("es año bisiesto")



if month < 1 or month > 12:
    print("La fecha no vale")
else:
    # Determinar la cantidad de días en el mes
    print(day, "/", month, "/", year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_dias = 31
        if (day < 0 or day > 31):
            print("Los días no son válidos")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_dias = 30
        if (day < 0 or day > 30):
            print("Los días no son válidos")
    elif month == 2:
        max_dias = 29 if bisis else 28
        if (day < 0 or day > max_dias):
            print("Los días no son válidos")
    else:
        max_dias = 0
        
#hora
numbaa2 = int(input("Ingrese la hora hhmmss: "))
second = numbaa2 % 100
minute = (numbaa2 // 100) % 100
hour = (numbaa2 // 10000) % 100

if (hour < 0 or hour > 23) or (minute < 0 or minute > 59) or (second < 0 or second > 59):
    print("La hora no es válida")
else:
    print(hour, ":", minute, ":", second)


#segundos_del_usuario y cálculo de segundos_del_usuario
segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
if segundos_usuario < 0:
    print("La cantidad de segundos no es válida")
else:
    ops = segundos_usuario + second
    if ops >= 60:
        minute = minute + (ops // 60)  # Agregar los minutos enteros
        ops = ops % 60  # Mantener solo los segundos restantes
    if minute >= 60:
        hour = hour + (minute // 60)  # Agregar las horas enteras
        minute = minute % 60  # Mantener solo los minutos restantes
    if hour >= 24:
        hour = hour - 24
        day = day + 1
    print("La hora es: ", hour, ":", minute, ":", ops)
    print("La fecha es: ", day, "/", month, "/", year)
