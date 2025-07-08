import pygame
from juego import *
from Costantes import *
from funciones import *

def mostrar_menu(pantalla: pygame.Surface):
    #fondito
    fondo_menu = pygame.image.load("fondo.jpg")
    fondo_menu = pygame.transform.scale(fondo_menu, PANTALLA)
    #objetos creados
    boton_jugar = crear_elemento_juego("boton_menu.png", ANCHO_BOTON, ALTO_BOTON, 85, 100)
    boton_opcionnes = crear_elemento_juego("boton_menu.png", ANCHO_BOTON, ALTO_BOTON, 85, 180)
    boton_ranking = crear_elemento_juego("boton_menu.png", ANCHO_BOTON, ALTO_BOTON, 85, 260)
    boton_salir = crear_elemento_juego("boton_menu.png", ANCHO_BOTON, ALTO_BOTON, 85, 340)

    
    en_menu = True
    while en_menu:
        #mostrar en pantalla
        pantalla.blit(fondo_menu, (0, 0))

        pantalla.blit(boton_jugar["superficie"], boton_jugar["rectangulo"])
        pantalla.blit(boton_opcionnes["superficie"], boton_opcionnes["rectangulo"])
        pantalla.blit(boton_ranking["superficie"], boton_ranking["rectangulo"])
        pantalla.blit(boton_salir["superficie"], boton_salir["rectangulo"])
        
        #mostrar el texto en cada objeto
        mostrar_texto(boton_jugar["superficie"], "JUGAR",(100,18), FUENTE_TEXTO,COLOR_NEGRO)
        mostrar_texto(boton_opcionnes["superficie"], "OPCIONES",(90,18), FUENTE_TEXTO,COLOR_NEGRO)
        mostrar_texto(boton_ranking["superficie"], "RANKING",(100,18), FUENTE_TEXTO,COLOR_NEGRO)
        mostrar_texto(boton_salir["superficie"], "SALIR",(110,18), FUENTE_TEXTO,COLOR_NEGRO)

        #cola de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_jugar["rectangulo"].collidepoint(evento.pos):
                        return "jugar"
                    if boton_ranking["rectangulo"].collidepoint(evento.pos):
                        return "ranking"
                    if boton_opcionnes["rectangulo"].collidepoint(evento.pos):
                        return "opciones"
                    elif boton_salir["rectangulo"].collidepoint(evento.pos):
                        return "salir"
                    

        pygame.display.flip()