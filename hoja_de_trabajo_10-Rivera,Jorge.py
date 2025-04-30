"""
#Hoja de Trabajo 10 Clases-----------------------------------------------------
#Ejercicio 1:
class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

class Perro(Animal):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

class Gato(Animal):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

class Ave(Animal):
    def __init__(self, nombre, edad, especie, volar):
        super().__init__(nombre, edad, especie)
        self.volar = volar
        
class Reptil(Animal):
    def __init__(self, nombre, edad, especie, escama):
        super().__init__(nombre, edad, especie)
        self.escama = escama

perro_1 = Perro("El Cholo", 7, "Pitbull", "Labrador")
gato_1 = Gato("Cori", 8, "Albino", "Blanco")
ave_1 = Ave("El Americano", 2, "águila", True)
reptil_a = Reptil("MG", 14, "Lagarto", True)

print(f"Perro: {perro_1.nombre}, {perro_1.edad} años, {perro_1.especie}, Raza: {perro_1.raza}")
print(f"Gato: {gato_1.nombre}, {gato_1.edad} años, {gato_1.especie}, Color: {gato_1.color}")
print(f"Ave: {ave_1.nombre}, {ave_1.edad} años, {ave_1.especie}, Puede volar: {ave_1.volar}")
print(f"Reptil: {reptil_a.nombre}, {reptil_a.edad} años, {reptil_a.especie}, Color escamas: {reptil_a.escama}")


#Ejercicio 2, identificación de personas:
class Persona:
    def __init__(self, nombre, edad, genero, dpi):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.dpi = dpi

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, dpi, carnet, carrera):
        super().__init__(nombre, edad, genero, dpi)
        self.carnet = carnet
        self.carrera = carrera
        
class Profesor(Persona):
    def __init__(self, nombre, edad, genero, dpi, codigo, facultad):
        super().__init__(nombre, edad, genero, dpi)
        self.codigo = codigo
        self.facultad = facultad

     
class Administrativo(Persona):
    def __init__(self, nombre, edad, genero, dpi, nivel):
        super().__init__(nombre, edad, genero, dpi)
        self.nivel = nivel


estudiante_a = Estudiante("Juan", 20, "Masculino", "1234567890123", "20200001", "Ingeniería en Sistemas")
Profesor_b = Profesor("Pedro", 45, "Masculino", "1234567890124", "12345", "Ingeniería")
admin_c = Administrativo("María", 35, "Femenino", "1234567890125", 5)

print(f"Estudiante: {estudiante_a.nombre}, {estudiante_a.edad} años, {estudiante_a.genero}, DPI: {estudiante_a.dpi}, Carnet: {estudiante_a.carnet}, Carrera: {estudiante_a.carrera}\n\nProfesor: {Profesor_b.nombre}, {Profesor_b.edad} años, {Profesor_b.genero}, DPI: {Profesor_b.dpi}, Código: {Profesor_b.codigo}, Facultad:{Profesor_b.facultad}\n\nAdministrativo: {admin_c.nombre}, {admin_c.edad} años, {admin_c.genero}, DPI: {admin_c.dpi}, Nivel:{admin_c.nivel}")
"""