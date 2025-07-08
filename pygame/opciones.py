import pygame
from menu import *
from funciones import *
from Costantes import *

def mostrar_opciones(pantalla: pygame.Surface):
    reloj = pygame.time.Clock()

    #verificar q este el volumen y cambia el estado
    musica_activada = pygame.mixer.music.get_volume() > 0
    volumen_actual = pygame.mixer.music.get_volume()

    #objetos creados
    boton_volver = crear_elemento_juego("mini_menu.png", ANCHO_MINI_BOTON, ALTO_MINI_BOTON, 10 , 5)
    boton_on = crear_elemento_juego("sonido.on.png", ANCHO_MUSICA, ALTO_MUSICA, 200, 250)
    boton_off = crear_elemento_juego("sonido.off.png", ANCHO_MUSICA, ALTO_MUSICA, 200, 250)
    boton_subir = crear_elemento_juego("suma.png", ANCHO_MUSICA, ALTO_MUSICA, 350, 250)
    boton_bajar = crear_elemento_juego("menos.png", ANCHO_MUSICA, ALTO_MUSICA, 50, 250)
    
    
    activo = True
    while activo:
        #se muestra en la pantalla
        pantalla.blit(fondo_pantalla, (0, 0))
        if musica_activada:
            pantalla.blit(boton_on["superficie"], boton_on["rectangulo"])
        else:
            pantalla.blit(boton_off["superficie"], boton_off["rectangulo"])

        pantalla.blit(boton_subir["superficie"], boton_subir["rectangulo"])
        pantalla.blit(boton_bajar["superficie"], boton_bajar["rectangulo"])
        pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])

        
        mostrar_texto(pantalla, f"Volumen actual: {int(volumen_actual * 100)}%", (125, 180), FUENTE_TEXTO, COLOR_NEGRO)

        #cola_eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_on["rectangulo"].collidepoint(evento.pos):
                        musica_activada = not musica_activada
                        volumen_actual = 0.3 if musica_activada else 0
                        pygame.mixer.music.set_volume(volumen_actual)
                        
                    elif boton_subir["rectangulo"].collidepoint(evento.pos):
                        volumen_actual = min(1.0, volumen_actual + 0.1)
                        pygame.mixer.music.set_volume(volumen_actual)
                        musica_activada = volumen_actual > 0
                        
                    elif boton_bajar["rectangulo"].collidepoint(evento.pos):
                        volumen_actual = max(0.0, volumen_actual - 0.1)
                        pygame.mixer.music.set_volume(volumen_actual)
                        musica_activada = volumen_actual > 0
                        
                    elif boton_volver["rectangulo"].collidepoint(evento.pos):
                        return "menu"
        pygame.display.flip()
        reloj.tick(FPS)
