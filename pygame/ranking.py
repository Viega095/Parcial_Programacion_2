import pygame
from Costantes import *
from funciones import *
def mostrar_ranking(pantalla: pygame.Surface):
    try:
        with open("partidas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos_ordenados = sorted(datos, key=lambda x: x["puntaje"], reverse=True)
    top_10 = datos_ordenados[:10]

    boton_mini_menu = crear_elemento_juego("mini_menu.png",ANCHO_MINI_BOTON, ALTO_MINI_BOTON, 10, 5)
    tabla_ranking = crear_elemento_juego("tabla_rank.png", 350, 400, 75,40)
    
    reloj = pygame.time.Clock()
    corriendo = True
    fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
    
    while corriendo:
        
        mostrar_texto(pantalla, "TOP 10 PUNTAJES", (100, 30), FUENTE_TEXTO, COLOR_BLANCO)

        y = 50
        for i, entrada in enumerate(top_10):
            texto = f"{i+1}. {entrada['nombre']} - {entrada['puntaje']} pts - {entrada['fecha']}"
            mostrar_texto(tabla_ranking["superficie"], texto, (23, y), FUENTE_RANKING, COLOR_BLANCO)
            y += 30

        
        pantalla.blit(fondo_pantalla, (0, 0))
        pantalla.blit(tabla_ranking["superficie"], tabla_ranking["rectangulo"])
        pantalla.blit(boton_mini_menu["superficie"], boton_mini_menu["rectangulo"])
        
        mostrar_texto(pantalla, "Presioná ESC para volver", (100, 460), FUENTE_TEXTO, COLOR_NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_mini_menu["rectangulo"].collidepoint(evento.pos):
                        return "menu" 
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()
        reloj.tick(FPS)