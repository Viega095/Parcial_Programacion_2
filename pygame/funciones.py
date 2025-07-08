import pygame
import json
from datetime import datetime
from Costantes import *
pygame.init()

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    """Mostrar texto en superficie

    Args:
        surface : Superficie en la que quieras escribir
        text : Texto que quieras poner en la malla
        pos : posicion del texto
        font : Fuente del texto
        color : Color de fuente del texto
    """
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        
def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    """Se encarga de crear un elemento en el juego guardando su superficie (textura) y su rectangulo (comportamiento) 

    Args:
        textura (str): Tiene que ser una ruta ya sea relativa o absoluta
        ancho (int): En pixeles el ancho de ese elemento
        alto (int): En pixeles el alto de ese elemento
        pos_x (int): Donde se va a ubicar en el eje x
        pos_y (int): Donde se va a ubicar en el eje y

    Returns:
        dict: El diccionario con el elemento creado
    """
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = pygame.Rect(pos_x,pos_y,ancho,alto)
    
    return elemento_juego

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int):
    """Podes limpiar la superficie que se pasa al parametro ya sea boton o fondo

    Args:
        elemento_juego (dict): que superficie queres limpiar (ejemplo boton_??["superficie"])
        textura (str): por cual textura lo queres reemplazas 
        ancho (int): ancho de la superficie
        alto (int): alto de la superficie
    """
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    

def reiniciar_datos():
    """Esta funcion se dedica a reiniciar todos los datos presentados

    Returns:
        datos: Reinicia vidas, puntaje y tiempo
    """
    datos = {"vida": VIDAS, "puntaje": PUNTAJE, "tiempo": TIEMPO_JUEGO}
    return datos


def guardar_en_json(nombre, puntaje):
    """Funcian dedicada a guardar las partidas en un apartado json para despues mostrar en una tabla

    Args:
        nombre (_type_): El nombre del jugador
        puntaje (_type_): Puntaje que llego el jugador en el juego
    """
    try:
        with open("partidas.json", "r", encoding="utf-8") as archivo:
            partidas = json.load(archivo)
    except FileNotFoundError:
        partidas = []

    nueva_partida = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    }

    partidas.append(nueva_partida)

    with open("partidas.json", "w", encoding="utf-8") as archivo:
        json.dump(partidas, archivo, indent=4)
        
def ocultar_boton(boton: dict):
    """Cree este boton mas que nada para ocultar las posiciones 

    Args:
        boton (dict): Se pasa el parametro de que boton queres ocultar
    """
    boton["rectangulo"].x = -1000
    boton["rectangulo"].y = -1000
    
