import math
#Hoja de trabajo 11-----------------
""" 
Ejercicio 1: Simulación de Experimentos de Caída Libre
- Crear una clase ExperimentoFisico con método abstracto realizar_experimento().
- una subclase CaidaLibre que:
• Atributos: Tenga atributos altura, gravedad
• Métodos: Calcule el tiempo de caída:
o 𝑡 = √2∗ℎ/𝑔
• Excepciones: Lance una excepción si la altura es negativa o la gravedad cero.
"""
class ExperimentoFisico:
    def realizar_experimento(self):
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad, tiempo):
        self.altura = altura
        self.gravedad = gravedad
        self.tiempo = tiempo

    def calculus(self):
        try:
            if self.altura < 0:
                raise ValueError("La altura no puede ser negativa")
            elif self.gravedad == 0:
                raise ValueError("La gravedad no puede ser cero")
            else:
                self.tiempo = math.sqrt((2 * self.altura) / self.gravedad)
                print("El tiempo de caída es: ", self.tiempo, "segundos")
        except ValueError as e:
            print(e)

#ops = CaidaLibre(25, 9.8, 0).calculus
#print(ops)
try:
    CaidaLibre(25, 9.8, 0).calculus()
except NameError:
    print("Error: Algún dato es incorrecto")

 #Ejercicio 2: Calculadora Científica
"""
Propósito: Construir una calculadora que agrupe operaciones científicas.
Descripción:
1. Clase base OperacionCientifica con un método calcular().
2. Subclases:
o RaizCuadrada
o Potencia
o Logaritmo
o Factorial
3. Capturar excepciones como:
o Raíz de número negativo
o Logaritmo de número no positivo
o Factorial de número negativo o no entero
"""
class OperacionCientifica:
    def calcular(self):
        pass
# Raíz Cuadrada
class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero, resultado):
        self.numero = numero
        self.resultado = resultado

    def calculus(self):
        try:
            if self.numero < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
            else:
                self.resultado = math.sqrt(self.numero)
                print("La raíz cuadrada de", self.numero, "es", self.resultado)
        except ValueError as e:
            print(e)
# Potencia
class Potencia(OperacionCientifica):
    def __init__(self, base, exponente, resultado):
        self.base = base
        self.exponente = exponente
        self.resultado = resultado
    def calculus(self):
        try:
            if self.base < 0:
                raise ValueError("No se puede calcular la potencia de un número negativo")
            else:
                self.resultado = math.pow(self.base, self.exponente)
                print("La potencia de", self.base, "elevado a", self.exponente, "es", self.resultado)
        except ValueError as e:
            print(e)
# Logaritmo
class Logaritmo(OperacionCientifica):
    def __init__(self, numero, resultado):
        self.numero = numero
        self.resultado = resultado
    def calculus(self):
        try:
            if self.numero <= 0:
                raise ValueError("No se puede calcular el logaritmo de un número negativo o cero")
            else:
                self.resultado = math.log(self.numero)
                print("El logaritmo de", self.numero, "es", self.resultado)
        except ValueError as e:
            print(e)
# Factorial
class Factorial(OperacionCientifica):
    def __init__(self, numero, resultado):
        self.numero = numero
        self.resultado = resultado
        self.cumulator = 1
    def calculus(self):
        try:
            if self.numero < 0:
                raise ValueError("No se puede calcular el factorial de un número negativo")
            else:
                while self.cumulator <= self.numero:
                    self.resultado *= self.cumulator
                    self.cumulator += 1
                print("El factorial de", self.numero, "es", self.resultado)
        except ValueError as e:
            print(e)

