"""
1.] Escribe un programa que extraiga la primera y la última palabra de una oración. Split()

Entrada: "Python es un lenguaje poderoso"
Salida: "Primera palabra: Python, Última palabra: poderoso"
"""
#palabra = "Python es un lenguaje poderoso"
#palabra_separada = palabra.split()
#print("\nPrimera palabra: {}\nSegunda Palabra: {}\n".format(palabra_separada[0], palabra_separada[-1]))


"""
-----------------------------------------------------------------------------------------------------------------------------------
2.] Crea un programa que elimine los espacios repetidos en una cadena

Entrada: "Hola  mundo  en  Python"
Salida: "Hola mundo en Python"


message = "Hola  mundo  en  Python"

ans = " ".join(message.split())
space_id = message.find("  ")
if space_id:
    message = message.replace("  ", " ")
    print(message)

-----------------------------------------------------------------------------------------------------------------------------------
3.] Dado un correo electrónico, extrae solo el dominio.
Entrada: "usuario@gmail.com"
Salida: "gmail.com"
split('@')

og_mail =  "usuario@gmail.com"
splited_mail = og_mail.split("@")

print(splited_mail[1])
-----------------------------------------------------------------------------------------------------------------------------------
4.] Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf).
Entrada: "documento.pdf"
Salida: True
Entrada: "imagen.jpg"
Salida: False


v1 = "documento.pdf"
v2 =  "imagen.jpg"
splited_v1 = v1.split(".")
splited_v2 = v2.split(".")

if splited_v1[1].endswith("pdf"):
    print("v1: True")
else:
    print("v1: False")

if splited_v2[1].endswith("pdf"):
    print("v2: True")
else:
    print("v2: False")
--------------------------------------------------------------------------------------------------------------------------------------
5. Dado un texto, invierte el orden de las palabras
Entrada: "Me gusta Python"
Salida: "Python gusta Me"
Usa split() y join() en combinación con [::-1]

palabra_og = "Me gusta Python"
palabra_og_splited = palabra_og.split()
palabra_reunited = " ".join(palabra_og_splited[::-1])

print(palabra_reunited)
--------------------------------------------------------------------------------------------------------------------------------------
6.] Dado un texto ingresado por el usuario detectar palabras claves y responder:
ejemplo:
texto de entrada: necesito que me escribas un poema de amor.
texto de entrada: escribe una canción de alegría.
De manera estática tendremos varias cadenas (5 a lo mucho) con palabras claves ejemplo:
poema1=”"Podrá nublarse el sol eternamente;
Podrá secarse en un instante el mar;
Podrá romperse el eje de la tierra
Como un débil cristal.”
canto1="Eres como la noche, callada y constelada.
Tu silencio es de estrella, tan lejano y sencillo.
Me gustas cuando callas porque estás como ausente.
Distante y dolorosa como si hubieras muerto."
Según la frase ingresada por el usuario detectar palabras claves y mostrar en pantalla lo solicitado.

poemas = ["Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra, como un débil cristal.",
 "Tu mirada es mi refugio, tu risa mi canción, en tus brazos encuentro paz, y en tu amor, mi razón."]
canciones = ["Eres como la noche, callada y constelada. Tu silencio es de estrella, tan lejano y sencillo. Me gustas cuando callas porque estás como ausente. Distante y dolorosa como si hubieras muerto.",
"Viento del desierto, susurras al sol, en la arena dorada, se esconde mi voz. El cielo se quema, la tierra se apaga, pero en mi alma, la esperanza no se va. Cruzando las dunas, bajo el sol abrasador, el desierto me llama, en su vasto fervor. Un oasis en el alma, y en el corazón, un suspiro de vida, un eco de pasión."]

ultimate_user_input = input("Coloque qué desea que escriba: ")
if ultimate_user_input.__contains__("poema") and ultimate_user_input.__contains__("amor") or ultimate_user_input.__contains__("amoroso"):
    print("Aquí está mi poema para ti: {}".format(poemas[1]))
elif ultimate_user_input.__contains__("poema"):
    print("Espero te guste este poema: {}".format(poemas[0]))
elif (ultimate_user_input.__contains__("canto") or ultimate_user_input.__contains__("canción")) and ultimate_user_input.__contains__("desierto"):
    print("Aquí está mi canción para ti: {}".format(canciones[1]))
elif (ultimate_user_input.__contains__("canto") or ultimate_user_input.__contains__("canción")):
    print("Escucha mi canción: {}".format(canciones[0]))
"""