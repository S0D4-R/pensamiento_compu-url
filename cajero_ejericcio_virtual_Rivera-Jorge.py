saldo_inicial = 3000
attempts = 3
while attempts >= 0:
    monto = int(input("Ingrese monto a retirar: "))
    if monto <= saldo_inicial:
        saldo_inicial -= monto
        print("Retiro exitoso. Nuevo saldo: Q", saldo_inicial)
        if saldo_inicial == 0:
            print("Ya no hay saldo disponible. Gracias por usar nuestros servicios.")
            break
    else:
        print("Saldo insuficiente. Intente nuevamente.")
        attempts -= 1
        if attempts == 0:
            print("Ha excedido el número máximo de intentos. Gracias por usar nuestros servicios.")
            break