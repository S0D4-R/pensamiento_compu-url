#Hoja de trabajo 9-----------------------------------------------------
#Ejercicio 1:
def par_o_impar(numero):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

#Ejercicio 2:
def sumar_listas(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

#Ejercicio 3:
def cuenta_regresiva(numero):
    if numero <= 0:
        print("Deploy")
    else:
        print(numero)
        cuenta_regresiva(numero - 1)

#Ejercicio 4:
def cuenta_ascendente(numero, greedy_one = 1):
    if greedy_one == numero:
        print(greedy_one)
    else:
        print(greedy_one)
        cuenta_ascendente(numero, greedy_one + 1)
    
#Ejercicio 5:
def suma_hasta(numero, acumulador = 1):
    x = 0
    y = 2
    keygen = True
    while keygen:
        if x == numero - 1:
            keygen = False
        print(acumulador)
        x += 1        
        acumulador += y
        y += 1
        

#Ejercicio 6:
#Función para factorial:
def factorial(num_limit, cumulator = 1, num_fact = 1):        
    if cumulator > num_limit:
        print(num_fact)
    else:
        num_fact *= cumulator
        cumulator += 1
        factorial(num_limit, cumulator, num_fact)

#Ejercicio 7:
#without_min
def minimum_lista(lista, x = None):
    for value in lista:
        if value < lista[0]:
            lista[0] = value
            minimum_lista(lista, x = lista[0])
    print(x)


# Recursividad el juego
def adivina_el_numero(numero_secreto, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Se acabaron los intentos! El número secreto era:", numero_secreto)
        return

    numero = input("Ingresa tu número: ")

    if numero.isdigit():
        numero = int(numero)
        if numero == numero_secreto:
            tiempo_total = time.time() - tiempo_inicio
            print(f"¡Felicidades! Adivinaste el número en {5 - intentos + 1} intento(s).")
            print(f"Tiempo total: {round(tiempo_total, 2)} segundos.")
            return
        elif numero < numero_secreto:
            print("Demasiado bajo.")
        else:
            print("Demasiado alto.")
        print(f"Te quedan {intentos - 1} intento(s).")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)
    else:
        print("Por favor, ingresa solo números.")
        adivina_el_numero(numero_secreto, intentos, tiempo_inicio)

# Iniciar el juego
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")
tiempo_inicio = time.time()
adivina_el_numero(80, 5, tiempo_inicio)