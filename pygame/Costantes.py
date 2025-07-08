import pygame
pygame.init()

#archivo para guardar las partidas
RUTA_ARCHIVO = "partidas.json"

#colores
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE_OSCURO = (64,145,108)
COLOR_ROJO = (255,0,0)
COLOR_ROJO_OSCURO = (164,110,110)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)

#recursos del juego
ANCHO  = 500
ALTO = 500
PANTALLA  = (ANCHO, ALTO)
FPS = 30
VIDAS = 3
PUNTAJE = 0
TIEMPO_JUEGO = 30
PUNTAJE_CORRECTO = 100
PUNTAJE_ERROR = -25
TIEMPO_AGREGADO = 5000 #5seg

#tama;os de botones
ANCHO_PREGUNTA = 400
ALTO_PREGUNTA = 130
ANCHO_RESPUESTA = 250
ALTO_RESPUESTA = 50
ANCHO_BOTON = 300
ALTO_BOTON  = 70
ANCHO_MUSICA = 90
ALTO_MUSICA = 90
ANCHO_MINI_BOTON = 50
ALTO_MINI_BOTON = 50
ANCHO_BOTON_COMODIN = 40
ALTO_BOTON_COMODIN = 40

#sonidos
CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("error.mp3")
CORRECTO_SONIDO = pygame.mixer.Sound("correcto.mp3")
VIDA_SONIDO = pygame.mixer.Sound("vida.mp3")
ESCUDO_ROTO = pygame.mixer.Sound("escudo.roto.mp3")

#fuentes
FUENTE_PREGUNTA = pygame.font.SysFont("Arial",28,True)
FUENTE_RESPUESTA = pygame.font.SysFont("Arial",18,True)
FUENTE_TEXTO = pygame.font.SysFont("Arial",25,True)
FUENTE_VOLUMEN = pygame.font.SysFont("Arial",50,True)
FUENTE_TIEMPO = pygame.font.SysFont("Arial",25,True)
FUENTE_TABLA = pygame.font.SysFont("Arial",18,True)
FUENTE_GRANDE = pygame.font.SysFont("Arial",45,True)
FUENTE_RANKING = pygame.font.SysFont("Arial",18,True)
#