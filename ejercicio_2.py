"""
En el año 2012 la municipalidad de Guatemala implementó un reglamento
que consiste en regular el tráfico y controlar la contaminación a través de
dejar circular o no a los vehículos según el caso:
Si el vehículo es del 2001 en adelante, la restricción depende del último dígito de
la placa:
• Si termina en 0, 2, 4, 6 u 8, NO circula los lunes.
• Si termina en 1, 3, 5, 7 o 9, NO circula los viernes.
• Si el año del vehículo es par, tiene una restricción adicional los sábados
solo circula hasta el mediodía.
Si el vehículo tiene más de 25 años de antigüedad, recibe una advertencia de
mantenimiento obligatorio.
"""
car_year = int(input("Ingrese el año del vehículo: "))
car_placa = input("Ingrese la placa del vehículo: ")
if car_year >= 2001:
    if car_placa.endswith("0") or car_placa.endswith("2") or car_placa.endswith("4") or car_placa.endswith("6") or car_placa.endswith("8"):
        print("No circula los lunes")
    elif car_placa.endswith("1") or car_placa.endswith("3") or car_placa.endswith("5") or car_placa.endswith("7") or car_placa.endswith("9"):
        print("No circula los viernes")
    if car_year % 2 == 0:
        print("No circula los sábados")
        print("Usted solo circula medio día")
else:
    print("Usted debe mantener o reemplazar su vehículo")