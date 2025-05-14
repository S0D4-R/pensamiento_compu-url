#proyecto lab 3:
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
niveles_azucar = [130, 160, 95, 175, 160] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [165, 130, 110, 125, 175] # mmHg

promedius_sugar = 0
promedius_salt = 0
promedius_presion = 0
semana = 1
print("---------------------------Semana 1-----------------------\n\n")
for i in range(len(dias)):
    promedius_sugar += niveles_azucar[i]
    promedius_salt += niveles_sal[i]
    promedius_presion += presion[i]
    print(f"♦{dias[i]}: Azúcar {niveles_azucar[i]} mg/dL, Sal {niveles_sal[i]} mg, Presión {presion[i]}\n")
    #Azúcar
    if niveles_azucar[i] > 140:
        print("    -Nivel de azúcar alto\n")
    elif niveles_azucar[i] < 70:
        print("    -Nivel de azúcar bajo\n")
    #sal
    if niveles_sal[i] > 2300:
        print("    -Nivel de sal alto, por favor reduzca la ingesta de sal\n")

    #presión sistólica
    if presion[i] > 120 and presion[i] < 130:
        print("    -Presión alta, por favor consulte a su médico\n")
    elif presion[i] > 130 and presion[i] < 140:
        print("    -Presión muy alta, por favor consulte a su médico, esto es hipertensión\n")
    elif presion[i] >= 140:
        print("    -Presión peligrosamente alta, por favor consulte a su médico, esto es hipertensión en etapa 2\n\n")

print("----------Promedio de los niveles de azúcar, sal y presión en la semana 1----------\n")
print("Promedio de azúcar: {}\nPromedio de sal: {}\nPresión promedio: {}\n\n".format(promedius_sugar/len(dias), promedius_salt/len(dias),promedius_presion/len(dias)))