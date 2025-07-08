from juego import * 
from menu import *
from ranking import *
from opciones import *
#iniciar
pygame.init()

#icono  y nombre
pygame.display.set_caption("Primer Juego titulo")
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

#SONIDOSS GLOBALES
pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#pantalla
pantalla = pygame.display.set_mode(PANTALLA)

datos = {"vida": VIDAS,
         "puntaje": PUNTAJE,
         "tiempo": TIEMPO_JUEGO}

while True:
    opcion = mostrar_menu(pantalla)
    if opcion == "jugar":
        datos = reiniciar_datos()
        resultado = jugar(pantalla, datos)
        if resultado == "fin":
            guardar_partida(pantalla, datos["puntaje"])
    elif opcion == "ranking":
        mostrar_ranking(pantalla)
    if opcion == "opciones":
        estado = mostrar_opciones(pantalla)
    elif opcion == "salir":
        break

pygame.quit()