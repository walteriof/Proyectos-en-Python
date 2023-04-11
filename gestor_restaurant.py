#*********************************************************************************
# Gestor de retaurant:
from tkinter import *
import random,datetime
from tkinter import filedialog,messagebox
operador = ""   # almacena todos los números presionados

precios_comida = [3000, 4000, 2000, 2600, 2900, 2700, 250, 300, 250]
precios_bebida = [250, 250, 300, 500, 600, 700, 1800, 1700, 300]
precios_postres = [500, 600, 650, 700, 550, 400, 450, 400, 300]
def click_boton(num):
    global operador
    operador += num
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)
def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0,END)
def resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ""
def revisar_check():    # se activa cada vez q se marque o desmarque un checkbox
    x = 0
    for c in cuadros_comida:
        if Var_comidas[x].get() == 1:   # si recibe la señal que se activa el checkbox
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get()== "0":
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1
    x = 0
    
    for c in cuadros_bebida:
        if Var_bebidas[x].get() == 1:   # si recibe la señal que se activa el checkbox
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get()== "0":
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x += 1
    
    x = 0
    for c in cuadros_postres:
        if Var_postres[x].get() == 1:   # si recibe la señal que se activa el checkbox
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get()== "0":
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x += 1
def total():
    sub_total_comida = 0
    precio = 0
    for cant in texto_comida:
        sub_total_comida += (float(cant.get()) * precios_comida[precio])
        precio += 1
    sub_total_bebida = 0
    precio = 0
    for cant in texto_bebida:
        sub_total_bebida += (float(cant.get()) * precios_bebida[precio])
        precio += 1
    sub_total_postres = 0
    precio = 0
    for cant in texto_postres:
        sub_total_postres += (float(cant.get()) * precios_postres[precio])
        precio += 1
    subtotal = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = subtotal * 0.105
    total = subtotal + impuestos

    var_costo_comida.set(f"$ {round(sub_total_comida,2)}")
    var_costo_bebida.set(f"$ {round(sub_total_bebida,2)}")
    var_costo_postres.set(f"$ {round(sub_total_postres,2)}")
    var_subtotal.set(f"$ {round(subtotal,2)}")
    var_impuestos.set(f"$ {round(impuestos,2)}")
    var_total.set(f"$ {round(total,2)}")
def recibo():           # cdo se oprime el boton recibo, se activa la función y ejecuta
    texto_recibo.delete(1.0,END)
    num_recibo = f"N°# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END,"*"*58+"\n")
    texto_recibo.insert(END, "Items\t\tcant.\tCosto Items\n")
    texto_recibo.insert(END,"-"*72+"\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":   # selecciono las comidas que hayan sido ordenadas
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t${int(comida.get())*precios_comida[x]}\n")
        x += 1
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":   # selecciono las bebidas que hayan sido ordenadas
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t${int(bebida.get())*precios_bebida[x]}\n")
        x += 1
    x = 0
    for postres in texto_postres:
        if postres.get() != "0":   # selecciono las postress que hayan sido ordenadas
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t${int(postres.get())*precios_postres[x]}\n")
        x += 1
    texto_recibo.insert(END,"-"*72+"\n")    # separador
    texto_recibo.insert(END,f" Costo de la comida: \t\t\t{var_costo_comida.get()}\n")   # cto total de comida
    texto_recibo.insert(END,f" Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")   # cto total de bebida 
    texto_recibo.insert(END,f" Costo de la postres: \t\t\t{var_costo_postres.get()}\n") # cto total de postre
    texto_recibo.insert(END,"-"*72+"\n")    # separador
    texto_recibo.insert(END,f" Subtotal: \t\t\t{var_subtotal.get()}\n")   # subtotal
    texto_recibo.insert(END,f" Impuestos: \t\t\t{var_impuestos.get()}\n")   # cto impuestos
    texto_recibo.insert(END,f" Total: \t\t\t{var_total.get()}\n")   # cto total
    texto_recibo.insert(END,"*"*58+"\n")
    texto_recibo.insert(END,"Muchas gracias por visitarnos\n")

def guardar():  # guardar ticket en arch .txt
    info_recibo = texto_recibo.get(1.0,END) # la var contiene toda la info del recibo desde el primer elem 1 hasta el final "end"
    archivo = filedialog.asksaveasfile(mode="w",defaultextension=".txt")    # filedialog servirá para crear el .txt
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Atención","Su recibo fue guardado exitosamente")    # mensaje de confirmación en ventana

def reset():    # borrar display
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:      # volver a 0 mensaje de comidas
        texto.set("0")
    for texto in texto_bebida:      # volver a 0 mensaje de bebidas
        texto.set("0")
    for texto in texto_postres:     # volver a 0 mensaje de postres
        texto.set("0")
    
    for cuadro in cuadros_comida:   # desactivar checkbox comidas
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:   # desactivar checkbox bebidas
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:  # desactivar checkbox postres
        cuadro.config(state=DISABLED)
    
    for var in Var_comidas:         # setear en 0 checkbox comidas
        var.set("0")
    for var in Var_bebidas:         # setear en 0 checkbox bebidas
        var.set("0")
    for var in Var_postres:         # setear en 0 checkbox postres
        var.set("0")
    
    var_costo_comida.set("")        # panel inferior q muestra el monto consumido en comidas, bebidas, postres, impuestos, etc
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_impuestos.set("")
    var_subtotal.set("")
    var_total.set("")
    
# iniciar tkinter
aplicacion = Tk()

# config del tamaño de la ventana:
aplicacion.geometry("1020x630+0+0")   # geometry pide parám de tamaño de la pantalla y ubicación (0(x)+0(y)) margen sup de la pantalla

# setear tamaño de pantalla por defecto para evitar cambios que rompan el diseño
aplicacion.resizable(0,0)

# cambiar titulo de la ventana
aplicacion.title("Restaurant - Sistema de facturación")
# cambiar color de fondo, ver tabla en: https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores 
aplicacion.config(bg="CadetBlue")

# recuadro panel superior de la app, con frame que otorga un marco general
panel_superior = Frame(aplicacion,bd=4,relief="sunken") # app, borde y relieve
panel_superior.pack(side=TOP)   # indico donde voy a poner el panel sup: arriba

# contenido_etiqueta_titulo:
etiqueta_titulo = Label(panel_superior,text="Sistema de facturación",fg="cadetblue",font=("Arial",40),bg="ivory2",width=27)
etiqueta_titulo.grid(row=0,column=0)  # .grid() es un formato de cuadrícula, debo indicarle fila y col

# panel izquierdo: menú
panel_izquierdo = Frame(aplicacion,bd=1,relief=FLAT)    # borde y relieve del panel
panel_izquierdo.pack(side=LEFT) # panel ubicado a la izquierda

# panel ctos:
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT,bg="azure4",padx=45)  # borde y relieve del panel ctos
panel_costos.pack(side=BOTTOM)  # panel ctos abajo y a la izquierda

# panel comidas:
panel_comidas = LabelFrame(panel_izquierdo, text="Comida",font=("Arial",12,"bold"),bd=1,relief=FLAT,fg="CornflowerBlue")    # LabelFrame() es como un cuadro con la etiqueta incorporada
panel_comidas.pack(side=LEFT)

# panel bedidas:
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",font=("Arial",12,"bold"),bd=1,relief=FLAT,fg="CornflowerBlue")    # LabelFrame() es como un cuadro con la etiqueta incorporada
panel_bebidas.pack(side=LEFT)

# panel postres:
panel_postres = LabelFrame(panel_izquierdo, text="Postres",font=("Arial",12,"bold"),bd=1,relief=FLAT,fg="CornflowerBlue")    # LabelFrame() es como un cuadro con la etiqueta incorporada
panel_postres.pack(side=LEFT)

# panel derecha:
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel_calculadora:
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_calculadora.pack()    # por defecto lo coloca arriba

# panel_recibo:
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_recibo.pack()    # por defecto lo coloca arriba

# panel_botones:
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg="burlywood")
panel_botones.pack()    # por defecto lo coloca arriba

# lista de productos:
lista_comidas = ["pollo asado","parrillada","pizza muzza","pizza especial","pizza 4 quesos","pizza verdeo","emp dulces","emp arabes","emp saladas"]
lista_bebidas = ["agua","soda","gaseosa","cerveza1","cerveza2","tragos","vino tinto","vino blanco","agua saborizada"]
lista_postres = ["helado","torta1","torta2","torta3","torta4","arroz con leche","flan","budin de pan","ens frutas"]

# items comidas
Var_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # checkbutton
    Var_comidas.append("")
    Var_comidas[contador] = IntVar()
    # crear check button:
    comida = Checkbutton(panel_comidas,text=comida.title(),font=("Arial",12,"bold"),onvalue=1,offvalue=0,variable=Var_comidas[contador],
                         command=revisar_check)
    
    comida.grid(row=contador,column=0,sticky=W)
    # crear cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()    # StringVar() signif var de tipo string
    texto_comida[contador].set("0")   # acá genera un error
    cuadros_comida[contador] = Entry(panel_comidas,font=("arial",11,"bold"),bd=1,width=6,state=DISABLED,textvariable=texto_comida[contador])    # cada elem de nuestra lista será un cuadro de entrada, state disabled para garantizar que no se ingrese la cant de comida hasta en tanto se tilde el cuadro 
    cuadros_comida[contador].grid(row=contador,column=1)
    contador += 1
# items bebidas
cuadros_bebida = []
texto_bebida = []
Var_bebidas = []
contador = 0
for bebida in lista_bebidas:
    # crear check buttons
    Var_bebidas.append("")
    Var_bebidas[contador] = IntVar()
    # crear check button:
    bebida = Checkbutton(panel_bebidas,text=bebida.title(),font=("Arial",12,"bold"),onvalue=1,offvalue=0,variable=Var_bebidas[contador],
                         command=revisar_check)   

    bebida.grid(row=contador,column=0,sticky=W)
    # crear cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()    # StringVar() signif var de tipo string
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,font=("Arial",11,"bold"),bd=1,width=6,state=DISABLED,textvariable=texto_bebida[contador])    # cada elem de nuestra lista será un cuadro de entrada, state disabled para garantizar que no se ingrese la cant de comida hasta en tanto se tilde el cuadro 
    cuadros_bebida[contador].grid(row=contador,column=1)
    contador += 1

# items postres
cuadros_postres = []
texto_postres = []
Var_postres = []
contador = 0
for postre in lista_postres:
    Var_postres.append("")
    Var_postres[contador] = IntVar()
    # crear check button:
    postre = Checkbutton(panel_postres,text=postre.title(),font=("Arial",12,"bold"),onvalue=1,offvalue=0,variable=Var_postres[contador],
                         command=revisar_check)   
    
    postre.grid(row=contador,column=0,sticky=W)
    #crear cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar()    # StringVar() signif var de tipo string
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,font=("Arial",11,"bold"),bd=1,width=6,state=DISABLED,textvariable=texto_postres[contador])    # cada elem de nuestra lista será un cuadro de entrada, state disabled para garantizar que no se ingrese la cant de comida hasta en tanto se tilde el cuadro 
    cuadros_postres[contador].grid(row=contador,column=1)
    contador += 1

# variables de costo comida:
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Etiquetas de costos y campos de entrada:
etiqueta_costo_comida = Label(panel_costos,text="Costo de Comida",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Etiquetas de costos y campos de entrada:
etiqueta_costo_bebida = Label(panel_costos,text="Costo de bebida",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_costo_bebida.grid(row=1,column=0)
texto_costo_bebida = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Etiquetas de postres y campos de entrada:
etiqueta_costo_postres = Label(panel_costos,text="Costo de postres",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_costo_postres.grid(row=2,column=0)
texto_costo_postres = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

# Etiquetas de subtotal y campos de entrada:
etiqueta_subtotal = Label(panel_costos,text="Subtotal",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_subtotal.grid(row=0,column=2)
texto_subtotal = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiquetas de impuestos y campos de entrada:
etiqueta_impuestos = Label(panel_costos,text="Impuestos",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_impuestos.grid(row=1,column=2)
texto_impuestos = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

# Etiquetas de total y campos de entrada:
etiqueta_total = Label(panel_costos,text="TOTAL",font=("arial",12,"bold"),bg="azure4",fg="white")
etiqueta_total.grid(row=2,column=2)
texto_total = Entry(panel_costos,font=("arial",12,"bold"),bd=1,width=10,state="readonly",textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones:
botones = ["total","recibo","guardar","reset"]
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("arial",10,"bold"),fg="white",bg="azure4",bd=1,width=10)
    botones_creados.append(boton)
    boton.grid(row=0,column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)

# area de recibo
texto_recibo = Text(panel_recibo,font=("arial",10,"bold"),bd=1,width=42,height=10)
texto_recibo.grid(row=0,column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,font=("arial",12,"bold"),width=32,bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)

botones_calculadora = ["7","8","9","+","4","5","6","-","1","2","3","x","enter","borrar","0","/"]
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,text=boton.title(),font=("arial",13,"bold"),fg="white",bg="azure4",bd=1,width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command = lambda : click_boton("7"))
botones_guardados[1].config(command = lambda : click_boton("8"))
botones_guardados[2].config(command = lambda : click_boton("9"))
botones_guardados[3].config(command = lambda : click_boton("+"))
botones_guardados[4].config(command = lambda : click_boton("4"))
botones_guardados[5].config(command = lambda : click_boton("5"))
botones_guardados[6].config(command = lambda : click_boton("6"))
botones_guardados[7].config(command = lambda : click_boton("-"))
botones_guardados[8].config(command = lambda : click_boton("1"))
botones_guardados[9].config(command = lambda : click_boton("2"))
botones_guardados[10].config(command = lambda : click_boton("3"))
botones_guardados[11].config(command = lambda : click_boton("*"))
botones_guardados[12].config(command = resultado)
botones_guardados[13].config(command = borrar)
botones_guardados[14].config(command = lambda : click_boton("0"))
botones_guardados[15].config(command = lambda : click_boton("/"))

# .mainloop() para evitar que finalice el código y la pantalla se cierre
aplicacion.mainloop()
