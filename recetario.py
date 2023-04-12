# Proyecto: administrador de recetas.
# ********************************************************************************
from pathlib import Path
import shutil
import os
import errno
import msvcrt
from os import system as limpiar_consola
limpiar_consola("cls")

def cant_txt(ruta):
    cant= 0
    # lista_txt = []
    # for i in Path(ruta).glob("**/*.txt"):  # el método .glob("*.txt") de manera recursiva permite recorrer todos (*) los .txt del directorio y subdirectorios (carpetas y sub carpetas)
    #     lista_txt.append(i)
    for i in Path(ruta).glob("**/*.txt"): # Mejor
        cant += 1                         # Mejor
    # cant = len(lista_txt)
    return cant

def crea_carpeta(ruta):
    os.chdir(ruta)      # establece a la ruta de la carpeta recetas como predeterminada
    salida = False
    while salida is False:
         try:
            nomb = input("Ingresa el nombre de la carpeta:\n")
            nva_carpeta = os.mkdir(nomb)
            mensaje = f"Su carpeta: '{nomb}' se ha creado correctamente"
            return nva_carpeta,mensaje
         except FileExistsError:
             print("Error: esa carpeta ya existe, prueba con otro nombre\n")
    return nva_carpeta

def muestra_txt(ruta):
    dicc_txt = {}
    dicc_ruta = {}
    for k,v in enumerate(Path(ruta).glob("*.txt")):  # el método .glob("*.txt") "global" permite recorrer todos (*) los .txt del directorio
        dicc_txt[k+1] = os.path.basename(v)
        dicc_ruta[k+1] = v
    return dicc_ruta,dicc_txt

def abrir_leer_escr(dir,accion):
    if accion == "leer":
        archivo = open(dir,"r",encoding="utf-8")
        nomb_receta = os.path.basename(dir)
        print("-"*10,f"[La receta {nomb_receta} dice:]","-"*10)
        print(archivo.read())
        archivo.close()
    elif accion == "escribir":
        archivo = open(dir,"a",encoding="utf-8")
        archivo.write(input("\nEscriba el contenido de la receta:\n"))
        archivo.close()
        return archivo

def confirma_borrar(ruta,tipo_arch):
    mensaje = ""
    salida = False
    while salida is False:
        confirma = input(f"Está seguro de borrar el arhivo '{os.path.basename(ruta)}'?. Responda [s - n]\n").lower()
        if confirma == "s" and tipo_arch == "txt":
            os.remove(ruta)   # Esto sirve para borrar archivo
            mensaje = "archivo borrado"
            salida = True
        elif confirma == "s" and tipo_arch == "carpeta":
            shutil.rmtree(ruta,ignore_errors=True,onerror=None)      # Esto sirve para borrar archivo
            mensaje = "archivo borrado"
            salida = True
        elif confirma == "n":
            salida = True
            mensaje = "archivo sin borrar"
        else:
            continue
    return mensaje

def ver_dir_recet(dir):     # función para ver las categorías en una lista
    dicc_dir_recet = {}
    with os.scandir(dir) as categorias:
        for k,v in enumerate(categorias):
            dicc_dir_recet[k+1] = v.name
    return dicc_dir_recet

def elije_dir_recet(diccio,num):
    nomb_dir_recet = ""
    for k,v in diccio.items():
        if k == num:
            nomb_dir_recet = v
    return nomb_dir_recet

def verif_numb(diccio):     # verifica si la opción numérica elegida está entre las opciones disponibles
    salida = False
    num_elect = 0
    cant = len(diccio)
    while salida is False:
        try:
            num_elect = int(input(f"Elija una opción del 1 al {cant}: "))
        except ValueError:
             print("Error: debes ingresar algún número.\n")
        if num_elect in diccio.keys():
            salida = True
    return num_elect

def const_ruta(ruta,nomb_categ):
    # base_guia = Path(base,"europa","españa","barcelona",Path("sagrada_familia","nuevo_archivo.txt"))    # instancias de path
    nva_ruta = Path(ruta,nomb_categ)
    return nva_ruta

def crea_txt(ruta,nomb_categ):
    existe = False
    while not existe:       # con este bucle verifico si el nombre del archivo ya existe en la carpeta
        tipo = ".txt"
        nomb_ing = input("\nEscriba el nombre del nuevo archivo: ")
        nva_ruta = Path(ruta,nomb_categ,nomb_ing+tipo)
        if not os.path.exists(nva_ruta):           # con os.path.exists(nva_ruta) verifica si ya existe otro archivo con ese nombre
            arch_nvo = open(nva_ruta,"w",encoding="utf-8").close()
            existe = True
            return arch_nvo,nva_ruta
        else: 
            print("\nLo siento, ese nombre ya pertenece a una receta, elija otro.")

def imprime_diccio_esc(diccio):
    print("")
    for i,k in diccio.items():
        print(f"\t[{i}]--->'{k}'")
    print("")

saludo_inicio = "Bienvenido al recetario"
saludo_final = "Muchas gracias por visitar el programa del recetario."
base = Path.home()
ruta = Path(r"C:\Users\Walterio\Recetas")   # Mejora ---> ruta = Path(Path.home(),"Recetas")
salida = False
print("")
# *************** Presentación: ***************
print(saludo_inicio)
print("")
print(f"La ruta base de acceso al recetario es '{base}'")
print("Cantidad de recetas registradas:",cant_txt(ruta))
print("\n------> Presione una tecla para ingresar al Menú <------")
espera_teclazo = msvcrt.getch()
diccio_categ = ver_dir_recet(ruta)
print("")

# *************** Menú: ***************
while salida is False:
    limpiar_consola("cls")
    op_menu = {1:'Leer receta', 2:'Crear receta', 3:'Crear carpeta', 4:'Eliminar receta', 5:'Eliminar categoría', 6:'Salir del programa'}
    print("*"*50)
    print("\tMenú principal:")
    # for i,k in op_menu.items():
    #     print(f"\t[{i}]--->'{k}'")
    # print("")
    diccio_categ = ver_dir_recet(ruta)
    imprime_diccio_esc(op_menu)
    print("*"*50)
    categ_elegida = verif_numb(op_menu)
    print("")

    if categ_elegida == 1:
# *************** módulo 1: leer receta ***************
        print("*"*50)
        print("\tUd eligió leer una receta, ahora deberá escoger alguna de las siguientes carpetas:")
        imprime_diccio_esc(diccio_categ)
        print("*"*50)
        nomb_categ = elije_dir_recet(diccio_categ,verif_numb(diccio_categ))
        ruta = Path(r"C:\Users\Walterio\Recetas")
        nvo_dir = const_ruta(ruta,nomb_categ)
        txt_rutas,txt_opciones_leer = muestra_txt(nvo_dir)
        # print(txt_rutas,txt_opciones_leer)
        if not txt_opciones_leer:
            print("-"*50)
            print("\tNo Tiene recetas disponibles")
            print("\n------> Presione una tecla para continuar <------")
            print("-"*50)
            espera_teclazo = msvcrt.getch()
            continue
        else:
            imprime_diccio_esc(txt_opciones_leer)
            num_txt_elegido = verif_numb(txt_opciones_leer)
            ruta_txt_elegido = Path(txt_rutas[num_txt_elegido])
            accion = "leer"
            print("")
            abrir_leer_escr(ruta_txt_elegido,accion)
            print("\n------> Presione una tecla para continuar <------")
            espera_teclazo = msvcrt.getch()

    elif categ_elegida == 2:
# *************** módulo 2: crear receta ***************
        print("\tUd eligió crear una receta, ahora deberá escoger alguna de las siguientes carpetas:")
        imprime_diccio_esc(diccio_categ)
        nomb_categ = elije_dir_recet(diccio_categ,verif_numb(diccio_categ))
        print("")
        print("Estás en la carpeta:",nomb_categ)
        ruta = Path(r"C:\Users\Walterio\Recetas")
        nvo_txt,ruta_nvo_arch = crea_txt(ruta,nomb_categ)
        accion = "escribir"
        nvo_texto_escrito = abrir_leer_escr(ruta_nvo_arch,accion)
        print("")
        print(f"\tLa receta '{ruta_nvo_arch.stem}' se ha creado exitosamente")
        print("\n------> Presione una tecla para continuar <------")
        espera_teclazo = msvcrt.getch()
    elif categ_elegida == 3:
# *************** módulo 3: crear categoría/carpeta ***************
        print("\tUd eligió crear una carpeta, éste es el listado de las existentes:")
        imprime_diccio_esc(diccio_categ)
        nomb_carpeta,confirm = crea_carpeta(ruta)
        print(confirm)
        print("\n------> Presione una tecla para continuar <------")
        espera_teclazo = msvcrt.getch()

    elif categ_elegida == 4:
# *************** módulo 4: eliminar receta ***************
        print("\tEscoja una carpeta, donde se ubique el archivo a borrar:")
        imprime_diccio_esc(diccio_categ)
        nomb_categ = elije_dir_recet(diccio_categ,verif_numb(diccio_categ))
        print("La carpeta elegida es:",nomb_categ)
        nva_ruta = Path(ruta,nomb_categ)
        ruta_de_archs,txt_en_carpeta = muestra_txt(nva_ruta)
        print("Ingrese el número del archivo a borrar:")
        imprime_diccio_esc(txt_en_carpeta)
        num_txt_elegido = verif_numb(txt_en_carpeta)
        ruta_txt_elegido_borrar = Path(ruta_de_archs[num_txt_elegido])
        tipo_arch = "txt"
        conf_borrar_arch = confirma_borrar(ruta_txt_elegido_borrar,tipo_arch)
        print(conf_borrar_arch)
        print("\n------> Presione una tecla para continuar <------")
        espera_teclazo = msvcrt.getch()

    elif categ_elegida == 5:
# *************** módulo 5: eliminar categoría ***************
        print("\tEscoja alguna de las carpetas a eliminar:")
        imprime_diccio_esc(diccio_categ)
        nomb_categ = elije_dir_recet(diccio_categ,verif_numb(diccio_categ))
        print("La carpeta elegida es:",nomb_categ)
        nva_ruta = Path(ruta,nomb_categ)
        tipo_arch = "carpeta"
        conf_borrar_arch = confirma_borrar(nva_ruta,tipo_arch)
        print(conf_borrar_arch)
        print("\n------> Presione una tecla para continuar <------")
        espera_teclazo = msvcrt.getch()

    elif categ_elegida == 6:
# *************** módulo 6: finalizar programa ***************
        print("\t\tUd. está por salir")
        print("------> Presione una tecla para continuar <------")
        espera_teclazo = msvcrt.getch()
        salida = True
    else:
        print("Error: no es una respuesta válida")
print(saludo_final)
