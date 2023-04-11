# Juego Invasión espacial:

import pygame, pathlib,random,math,io
from pygame import mixer
# filepath = pathlib.Path(__file__).resolve().parent/"invasores.png"
# setear_imagen = pygame.image.load(filepath)
pygame.init()                          # primero se inicializa pygame

# fondo con color
pantalla = pygame.display.set_mode((800,600))   # quiero que pantalla sea = a establecer el modo en que se muestra pygame (ancho y alto en tupla)

# título e ícono
pygame.display.set_caption("Invasión espacial")  # set_caption establece como será el título que aparecerá arriba de la ventana
icono = pygame.image.load(r"D:\\WALTERIO\\Waltério\\Tecnicatura en programación\\Lab de computación 1\\python\\Curso_Python_total\\ovni.png") # con image.load cargamos la ruta del ícono en una variable, no está funcionando
pygame.display.set_icon(icono)                   # display.set_icon colocamos el ícono en la ventana del display
fondo = pygame.image.load("D:\\WALTERIO\\Waltério\\Tecnicatura en programación\\Lab de computación 1\\python\\Curso_Python_total\\escena-galaxia_800x600px.jpg")

# música de fondo:
mixer.music.load(r"D:\WALTERIO\Waltério\Tecnicatura en programación\Lab de computación 1\python\Curso_Python_total\starwars.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)    # -1 para decirle que se ejecute siempre como en un loop

# variables de los enemigos
img_enemigo = []
enemigo_X = []
enemigo_Y = []
enemigo_X_cambio = []
enemigo_Y_cambio = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    # variable enemigo
    img_enemigo.append(pygame.image.load("D:\\WALTERIO\\Waltério\\Tecnicatura en programación\\Lab de computación 1\\python\\Curso_Python_total\\enemigo_2_45px.png"))
    enemigo_X.append(random.randint(0,736))
    enemigo_Y.append(random.randint(50,200))
    enemigo_X_cambio.append(0.5)
    enemigo_Y_cambio.append(50)

def enemigo(x,y,num_enemigo):
    pantalla.blit(img_enemigo[num_enemigo],(x,y))   # funcion enemigo

# variable bala
img_bala = pygame.image.load("D:\\WALTERIO\\Waltério\\Tecnicatura en programación\\Lab de computación 1\\python\\Curso_Python_total\\bala_16px.png")
bala_X = 0                      # eje X:
bala_Y = 500                    # eje Y: se establece una pos casi en la punta de la nave 
bala_X_cambio = 0               # no es necesaria una tasa de cambio de dirección en el eje x
bala_Y_cambio = 2               # tasa de cambio para el eje Y
bala_visible = False

# puntaje:
puntaje = 0
fuente = pygame.font.Font(r"D:\WALTERIO\Waltério\Tecnicatura en programación\Lab de computación 1\python\Curso_Python_total\Arcade.ttf",32)
texto_x = 10    # ubic del texto puntaje eje x
texto_y = 10    # ubic del texto puntaje eje y
# texto game over:
fuente_game_over = pygame.font.Font(r"D:\WALTERIO\Waltério\Tecnicatura en programación\Lab de computación 1\python\Curso_Python_total\Arcade.ttf",70)

# def fuente_bytes(fuente):           # quedó sin uso, no pude pasarlo a ejecutable
#     with open(fuente,"rb") as f:    # abre el arch ttf en modo de lectura binaria
#         ttf_bytes = f.read()        # lee todos los bytes del archivo y los almacena en la var
#     return io.BytesIO(ttf_bytes)    # crea y devuelve un obj BytesIO en base a los bytes del ttf

def texto_final():
    fuente_final = fuente_game_over.render("GAME OVER: ALIEN'S WIN",True,(255,0,0))
    pantalla.blit(fuente_final,(20,200))    # el centro de la pantalla es x=300, y=200

# función mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}",True,(255,255,255)) # otros colores: (235, 194, 122)
    pantalla.blit(texto,(x,y))

# Función disparar bala:
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10))
# función detectar colisiones:
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    if distancia < 27:
        return True
    else:
        return False

# variables del jugador
img_jugador = pygame.image.load("D:\\WALTERIO\\Waltério\\Tecnicatura en programación\\Lab de computación 1\\python\\Curso_Python_total\\astronave.png")
jugador_X = 368                        # se establece la posición del jugador en el eje X, para que quede al medio debo restar la mitad del tamaño del icono a 400, en 368 aparece bien
jugador_Y = 536                        # se establece la posición del jugador en el eje Y, para que quede al medio debo restar el tamaño del icono a 600, en 536 esta bien
jugador_X_cambio = 0                   # almacena el valor de cambio en la pos del eje de las X

def jugador(x,y):                      # función jugador que construye la pos del personaje
    pantalla.blit(img_jugador,(x,y))   # blit() significa algo como arrojar para establecer al jugador en al pantalla, se le pasa la imagen del jugador y la pos en una tupla (ejeX, ejeY)


ejecutar = True                        # variable centienla
while ejecutar:                        # bucle que muestra la pantalla hasta que cerramos la ventana
    pantalla.blit(fondo,(0,0))         # blit toma la var img y las coord 0x 0y para que cubra toda la pantalla
    # pantalla.fill((235, 194, 122))     # para setear un color de fondo, formato RGB, necesita de actualizarse con update, reemplazado por img de fondo
    # jugador_X += 0.1                   # por cada iteración la nave se mueve 1px a la derecha
    # jugador_X -= 0.1                   # por cada iteración la nave se mueve 1px a la izquierda
    # jugador_Y -= 0.1                   # por cada iteración la nave se mueve 1px hacia arriba
    # enemigo_X += 0.1
    for i in pygame.event.get():        # itera por cada evento que suceda en pygame
        if i.type == pygame.QUIT:       # cerrar el juego: si el evento es de tipo quit, o sea si cerramos la pantalla
            ejecutar = False            # ejecutar pasa a ser false y podemos salir de la pantalla
        if i.type == pygame.KEYDOWN:    # presionar flecha: pygame.KEYDOWN significa tecla presionada, puede ser cualquiera
            # print("Otra tecla fue oprimida")
            if i.key == pygame.K_LEFT:  # si la tecla presionada fue la flecha izquierda
                jugador_X_cambio -= 0.6 # cdo presione la tecla se corre a la izquiera
            elif i.key == pygame.K_RIGHT:
                jugador_X_cambio += 0.6 # cdo presione la tecla se corre a la derecha
            elif i.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound(r"D:\WALTERIO\Waltério\Tecnicatura en programación\Lab de computación 1\python\Curso_Python_total\disparo.mp3")
                sonido_disparo.play()
                if not bala_visible:
                    bala_X = jugador_X
                disparar_bala(bala_X,bala_Y)
        if i.type == pygame.KEYUP:      # Soltar flecha: verifica si el usuario soltó la tecla
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                jugador_X_cambio = 0    # al dejar de oprimir la tecla se queda quieto

# modifica la ubic del enemigo
    for i in range(cantidad_enemigos):
        # fin del juego
        if enemigo_Y[i] > 500:
            for k in range(cantidad_enemigos):
                enemigo_Y[k] = 1000
            texto_final()
            break
        enemigo_X[i] += enemigo_X_cambio[i]
    # bordes del enemigo
        if enemigo_X[i] >= 768:
            enemigo_X_cambio[i] = -0.5
            enemigo_Y[i] += enemigo_Y_cambio[i]
        elif enemigo_X[i] <= 0:
            enemigo_X_cambio[i] = 0.5
            enemigo_Y[i] += enemigo_Y_cambio[i]
        # se invoca la función colisión
        colision = hay_colision(enemigo_X[i],enemigo_Y[i],bala_X,bala_Y) 
        if colision:                        # si hay colisión, se debe recargar bala y bala deja de estar visible
            sonido_colision = mixer.Sound(r"D:\WALTERIO\Waltério\Tecnicatura en programación\Lab de computación 1\python\Curso_Python_total\Golpe.mp3")
            sonido_colision.play()
            bala_Y = 500
            bala_visible = False
            puntaje += 1
            # print("Puntaje:",puntaje)
            enemigo_X[i] = random.randint(0,736)    # cdo la bala le pega, se reinicia la posición del enemigo en pantalla
            enemigo_Y[i] = random.randint(50,200)
        enemigo(enemigo_X[i],enemigo_Y[i],i)
        
    # modifica la ubic del jugador
    jugador_X += jugador_X_cambio       # hacemos q jugador x se mueva tanto como le indique la var de cambio (jugador_X_cambio)
    # bordes horiz jugador
    if jugador_X <= 0:                  # poner topes a los bordes horiz para que no sean menor a 0 ni mayor a 736 
        jugador_X = 0
    elif jugador_X >= 736:
        jugador_X = 736

    # reinicio el disparo de bala
    if bala_Y <= -16:
        bala_Y = 500
        bala_visible = False

    # movimiento de la bala:
    if bala_visible == True:
        disparar_bala(bala_X,bala_Y)
        bala_Y -= bala_Y_cambio

    mostrar_puntaje(texto_x,texto_y)
    
    jugador(jugador_X,jugador_Y)        # la llamada a la func del jugador tiene q aparecer antes de actualizar, para q se vea
    pygame.display.update()             # actualiza el color de fondo de la pantalla y lo muestra
