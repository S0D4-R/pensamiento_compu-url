"""
# Ejercicio 1:
for i in range(1, 12):
    if i % 2 != 0:
        print(i)

# Ejercicio 2:
x = 1
while x <= 11:
    if x % 2 != 0:
        print(x)
    x += 1

# Escenario 1:
while True:
    code_temp = input("Escriba una palabra: ")
    if code_temp == "chupacabra":
        print("¡Has dejado el bucle con éxito!")
        break

# Escenario 2:
vocals = ["A", "E", "I", "O", "U"]
user_word = input("Cloque un texto: ")
user_wordX = user_word.upper()
for letter in user_wordX:
    if letter in vocals:
        continue
    print(letter)
"""