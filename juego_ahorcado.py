# juego del ahorcado:
from random import choice
from os import system as limpiar_pantalla
import string
palabras = ["cultura",	"autor",	"actuacion",	"espectador",	"espectaculo",	"entretenimiento",	"arte",	"cine",	"dibujo",	"pintura",	"musica",	"religion",	"dios",	"articulo",	"educacion",	"escuela",	"instituto",	"colegio",	"universidad",	"clase",	"curso",	"estudio",	"formacion",	"analisis",	"investigacion",	"conocimiento",	"idea",	"informacion",	"dato",	"forma",	"manera",	"modo",	"estilo",	"figura",	"elemento",	"utilizacion",	"uso",	"ciencia",	"aritmetica",	"historia",	"geografia",	"fisica",	"deporte",	"carrera",	"competencia",	"competicion",	"ayuda",	"favor",	"apoyo",	"busqueda",	"duda",	"pregunta",	"respuesta",	"cuestion",	"solicitud",	"decision",	"eleccion",	"consejo",	"sugerencia",	"orden",	"control",	"sistema",	"trabajo",	"empleo",	"profesion",	"esfuerzo",	"humanidad",	"humano",	"persona",	"gente",	"hombre",	"mujer",	"bebe",	"adolescente",	"adulto",	"anciano",	"dona",	"caballero",	"dama",	"individuo",	"cuerpo",	"pierna",	"pie",	"talon",	"espinilla",	"rodilla",	"muslo",	"cabeza",	"cara",	"boca",	"labio",	"diente",	"ojo",	"nariz",	"barba",	"bigote",	"cabello",	"oreja",	"cerebro",	"estomago",	"brazo",	"codo",	"hombro",	"alimento",	"comida",	"bebida",	"vegetal",	"planta",	"pasto",	"flor",	"fruta",	"semilla",	"arbol",	"hoja",	"raiz",	"tallo",	"hongo",	"ciruela",	"pino",	"bambu",	"nuez",	"almendra",	"arroz",	"avena",	"cebada",	"trigo",	"verdura",	"papas",	"porotos",	"rabano",	"zanahoria",	"manzana",	"naranja",	"platano",	"pera",	"mano",	"palma",	"dedo",	"trasero",	"abdomen",	"higado",	"musculo",	"cuello",	"corazon",	"mente",	"alma",	"espiritu",	"pecho",	"cintura",	"cadera",	"espalda",	"sangre",	"carne",	"piel",	"hueso",	"resfriado",	"gripe",	"diarrea",	"salud",	"enfermedad",	"durazno",	"tomate",	"sandia",	"carne",	"gaseosa",	"cesped",	"guisantes",]

def elije_palabra(lista):
    dic_pal_secret = {}
    dic_guiones = {}
    lista_pala_descomp = []
    palabra_secreta = choice(lista)
    for i in palabra_secreta:                   # bucle para descomponer la palabra en letras dentro de una lista
        lista_pala_descomp.append(i)
    for i,letra in enumerate(palabra_secreta):  # bucle para pasar una palabra a un diccio con el índice como clave
        dic_pal_secret[i] = letra
        dic_guiones[i] = "-"
    return dic_pal_secret,dic_guiones

def confirm_char():             # sin parámetros
    salida = False
    while salida is False:
        letra = input("ingresa una letra: ").lower()
        if letra in string.ascii_lowercase:
            salida = True
        else:
            salida = False
    return letra

def letra_en_palabra(letra,dic_pal_secret,dic_guiones):
    yerros = 0
    mens_acierta_letra = ""
    if letra not in dic_pal_secret.values():
        yerros += 1
    else:
        for f,v in dic_pal_secret.items():
            if v == letra:
                dic_guiones[f] = v
                mens_acierta_letra = f"Acertaste con la {v}, vas bien"
    return dic_guiones,yerros,mens_acierta_letra

limpiar_pantalla('cls')
nombre = input("Dime tu nombre:\n")
saludo = f"Bienvenido/a '{nombre}', tienes 5 intentos para descubrir la palabra."
en_juego = True
fin_de_vidas = 0
mensaje_vidas = 0
mensaje = ""
mensaje_final = ""
palabra_oculta,palabra_en_guiones= elije_palabra(palabras)
print("")
print(saludo)
print(f"Debes adivinar la siguiente palabra de {list(palabra_en_guiones.values())} letras")

while en_juego is True and fin_de_vidas < 5:

    print("")
    develando_palabra,errados,mens_acierto= letra_en_palabra(confirm_char(),palabra_oculta,palabra_en_guiones)
    print("")
    print(list(develando_palabra.values()))     # casteo el diccio a lista a ver si puedo evitar el mensaje del dicc

    if "-" in develando_palabra:
        en_juego = True
    elif mens_acierto != "":
        print(mens_acierto)
    elif errados == 1:
        fin_de_vidas += 1
        print(f"Fallaste, quedan {5-fin_de_vidas} intentos")
    if "-" not in develando_palabra.values():
        mensaje_final = f"Felicitaciones {nombre} has ganado y te sobraron {5-fin_de_vidas} intentos!!!"
        en_juego = False
    if fin_de_vidas == 5:
        mensaje_final = f"{nombre} has perdido :'(  no importa vuelve a intentarlo"
print("")
print(mensaje_final)
print("Fin del juego")
