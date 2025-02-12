'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''
def comvertaa(roma_nambaa):
    if roma_nambaa <= 3:
        print(roma_nambaa * "I")
    elif roma_nambaa == 4:
        print("IV")
    elif roma_nambaa >= 5 and roma_nambaa < 9:
        print("V" + (roma_nambaa - 5)*"I")
    elif roma_nambaa == 9:
        print("IX")


print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Bienvenido~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n")
roman__interprata = int(input("Ingese un número del 1 al 9: "))
if roman__interprata > 9:
    print("Ese número no está disponible, por favor escriba un número menor o igual a 9")
else:
    comvertaa(roman__interprata)