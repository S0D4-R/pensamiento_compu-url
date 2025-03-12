"""
Una empresa administradora de edificios quiere implementar un sistema para
calcular el costo del consumo de agua con base a la cantidad de metros cúbicos
utilizados y el número de habitantes en el apartamento.
Si el consumo es menor a 15 m³, la tarifa es Q5 por m³.
Si el consumo está entre 15 y 30 m³:
• Si hay más de 3 habitantes, la tarifa es de Q4 por m³.
• Si hay exactamente 3 habitantes, la tarifa es de Q4.5 por m³.
• En cualquier otro caso, la tarifa es de Q5 por m³.
Si el consumo es mayor a 30 m³:
• Si el número de habitantes es mayor a 5, la tarifa es de Q3.5 por m³.
• Si el número de habitantes es par, la tarifa es de Q4 por m³.
• En cualquier otro caso, la tarifa es de Q4.2 por m³.
"""
n_agua = float(input("Ingrese la cantidad de m³ utilizados: "))
n_habitantes = int(input("Ingrese el numero de habitantes: "))
if n_agua < 15:
    print(f"El costo de agua es de Q5 por m³, el total es de: Q.{5*n_agua}")
elif n_agua >= 15 and n_agua <= 30:
    if n_habitantes > 3:
        print(f"El costo de agua es de Q4 por m³, el total es de: Q.{4*n_agua}")
    elif n_habitantes == 3:
        print(f"El costo de agua es de Q4.5 por m³, el total es de: Q.{4.5*n_agua}")
    else:
        print(f"El costo de agua es de Q5 por m³, el total es de: Q.{5*n_agua}")
elif n_agua > 30:
    if n_habitantes > 5:
        print(f"El costo de agua es de Q3.5 por m³, el total es de: Q.{3.5*n_agua}")
    elif n_habitantes % 2 == 0:
        print(f"El costo de agua es de Q4 por m³, el total es de: Q.{4*n_agua}")
    else:
        print(f"El costo de agua es de Q4.2 por m³, el total es de: Q.{4.2*n_agua}")