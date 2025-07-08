import pygame
import random
from preguntas_generadas import *
from Costantes import *
from funciones import *

#OBJETOS
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
cuadro_pregunta = crear_elemento_juego("textura_pregunta.png", ANCHO_PREGUNTA, ALTO_PREGUNTA, 50, 55)

posiciones_respuestas = [200, 260, 320, 380]
botones_respuesta = []
for y in posiciones_respuestas:
    boton = crear_elemento_juego("textura_respuesta.png", ANCHO_RESPUESTA, ALTO_RESPUESTA, 120, y)
    botones_respuesta.append(boton)

menu_vida = crear_elemento_juego("boton_menu.png", 120, ALTO_MINI_BOTON,65,5)
boton_mini_menu = crear_elemento_juego("mini_menu.png",ANCHO_MINI_BOTON, ALTO_MINI_BOTON, 10, 5)

boton_bomba = crear_elemento_juego("bomba.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 40, 250)
boton_x2 = crear_elemento_juego("x2.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 400, 250)
boton_doble = crear_elemento_juego("doble.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 400, 350)
boton_pasar = crear_elemento_juego("pasar.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 40, 350)

#RELOJ = Nos permite controlar la cantidad de fps del juego
reloj = pygame.time.Clock()
#2

def jugar(pantalla: pygame.Surface, datos: dict) -> str:
    #banderas
    bandera_bomba = True
    bandera_x2 = True
    bandera_doble = True
    bandera_pasar = True
    
    x2 = False
    doble_activado = False
    respuesta_incorrecta = -1 
    indice_pregunta = 0
    racha_correctas = 0
    
    #copiamos las preguntas
    preguntas_disponibles = preguntas.copy()
    #las revolvemos xd
    random.shuffle(preguntas_disponibles)
    pregunta = preguntas_disponibles[indice_pregunta]
    
    tiempo_inicio = pygame.time.get_ticks()
    corriendo = True
    while corriendo:
        #ajustamos los fps
        reloj.tick(FPS)
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = max(0, datos["tiempo"] - (tiempo_actual - tiempo_inicio) // 1000)

        posiciones_originales = [(120, 200), (120, 260), (120, 320), (120, 380)]
        #cola de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_mini_menu["rectangulo"].collidepoint(evento.pos):
                        limpiar_superficie(cuadro_pregunta, "textura_pregunta.png", ANCHO_PREGUNTA, ALTO_PREGUNTA)
                        for boton in botones_respuesta:
                            limpiar_superficie(boton, "textura_respuesta.png", ANCHO_RESPUESTA, ALTO_RESPUESTA)
                        return "menu"
                    
                    if boton_bomba["rectangulo"].collidepoint(evento.pos) and bandera_bomba:
                        opciones_correcta = pregunta["respuesta_correcta"] -1
                        indices = [0, 1, 2, 3]
                        indices.remove(opciones_correcta)
                        eliminadas = random.sample(indices, 2)
                        for i in eliminadas:
                            ocultar_boton(botones_respuesta[i])
                        
                        
                        bandera_bomba = False
                        
                    if boton_x2["rectangulo"].collidepoint(evento.pos) and bandera_x2:
                        x2 = True
                        bandera_x2 = False
                        
                    if boton_doble["rectangulo"].collidepoint(evento.pos) and bandera_doble:
                        doble_activado = True
                        bandera_doble = False
                    
                    if boton_pasar["rectangulo"].collidepoint(evento.pos) and bandera_pasar:
                        bandera_pasar = False
                        limpiar_superficie(cuadro_pregunta, "textura_pregunta.png", ANCHO_PREGUNTA, ALTO_PREGUNTA)
                        for boton in botones_respuesta:
                            limpiar_superficie(boton, "textura_respuesta.png", ANCHO_RESPUESTA, ALTO_RESPUESTA)
                        
                        CLICK_SONIDO.play()
                        CLICK_SONIDO.set_volume(0.1)

                        indice_pregunta += 1
                        if indice_pregunta < len(preguntas_disponibles):
                            pregunta = preguntas_disponibles[indice_pregunta]
                            for i, boton in enumerate(botones_respuesta):
                                boton["rectangulo"].x, boton["rectangulo"].y = posiciones_originales[i]
                        else:
                            return "fin"
                        continue
                    
                    for i, boton in enumerate(botones_respuesta):
                        if boton["rectangulo"].collidepoint(evento.pos):
                            if (i+1) == pregunta["respuesta_correcta"]:
                                doble_activado = False
                                #sonidos de correcto
                                CORRECTO_SONIDO.play()
                                CORRECTO_SONIDO.set_volume(0.2)
                                if x2:
                                    datos["puntaje"] += PUNTAJE_CORRECTO * 2
                                    x2 = False
                                    tiempo_inicio += TIEMPO_AGREGADO * 2
                                else:
                                    datos["puntaje"] += PUNTAJE_CORRECTO
                                    tiempo_inicio += TIEMPO_AGREGADO
                                racha_correctas += 1
                                if racha_correctas == 5:
                                    datos["vida"] += 1
                                    racha_correctas = 0
                                    #vida extra ++
                                    VIDA_SONIDO.play()
                                    VIDA_SONIDO.set_volume(0.05)

                                    
                            else:
                                if doble_activado and respuesta_incorrecta == -1:
                                    ESCUDO_ROTO.play()
                                    ESCUDO_ROTO.set_volume(0.1)
                                    respuesta_incorrecta = i
                                    ocultar_boton(botones_respuesta[i]) 
                                    continue
                                else:
                                    #sonido de error
                                    ERROR_SONIDO.play()
                                    ERROR_SONIDO.set_volume(0.1)
                                    datos["puntaje"] += PUNTAJE_ERROR
                                    datos["vida"] -= 1
                                    racha_correctas = 0
                                
                            #limpiamos cada vez q contestamos
                            limpiar_superficie(cuadro_pregunta, "textura_pregunta.png", ANCHO_PREGUNTA, ALTO_PREGUNTA)
                            for boton in botones_respuesta:
                                limpiar_superficie(boton, "textura_respuesta.png", ANCHO_RESPUESTA, ALTO_RESPUESTA)
                            limpiar_superficie(menu_vida, "boton_menu.png", 120, ALTO_MINI_BOTON)
                            #SONIDOS DE CLICK
                            CLICK_SONIDO.play()
                            CLICK_SONIDO.set_volume(0.1)
                            
                            #verificamos la vida o si nos queda tiempo
                            if datos["vida"] <= 0 or tiempo_restante <= 0:
                                return "fin"
                            #cambiamos pregunta
                            indice_pregunta += 1
                            if indice_pregunta < len(preguntas_disponibles):
                                pregunta = preguntas_disponibles[indice_pregunta]
                                for i, boton in enumerate(botones_respuesta):
                                    boton["rectangulo"].x, boton["rectangulo"].y = posiciones_originales[i]
                            else:
                                return "fin"
        
        #dibujamos los objetos creados
        pantalla.blit(fondo_pantalla, (0, 0))
        pantalla.blit(cuadro_pregunta["superficie"], cuadro_pregunta["rectangulo"])
        for boton in botones_respuesta:
            pantalla.blit(boton["superficie"], boton["rectangulo"])
        #minibotones
        pantalla.blit(boton_mini_menu["superficie"], boton_mini_menu["rectangulo"])
        pantalla.blit(menu_vida["superficie"],menu_vida["rectangulo"])
        pantalla.blit(boton_bomba["superficie"], boton_bomba["rectangulo"])
        pantalla.blit(boton_x2["superficie"],boton_x2["rectangulo"])
        pantalla.blit(boton_doble["superficie"],boton_doble["rectangulo"])
        pantalla.blit(boton_pasar["superficie"],boton_pasar["rectangulo"])
        
        #mostramos los datos en ca  da objeto seleccionado
        mostrar_texto(cuadro_pregunta["superficie"], pregunta["pregunta"], (45, 25), FUENTE_PREGUNTA, COLOR_BLANCO)
        mostrar_texto(botones_respuesta[0]["superficie"], pregunta["opciones1"], (45, 15), FUENTE_RESPUESTA, COLOR_BLANCO)
        mostrar_texto(botones_respuesta[1]["superficie"], pregunta["opciones2"], (45, 15), FUENTE_RESPUESTA, COLOR_BLANCO)
        mostrar_texto(botones_respuesta[2]["superficie"], pregunta["opciones3"], (45, 15), FUENTE_RESPUESTA, COLOR_BLANCO)
        mostrar_texto(botones_respuesta[3]["superficie"], pregunta["opciones4"], (45, 15), FUENTE_RESPUESTA, COLOR_BLANCO)
        mostrar_texto(menu_vida["superficie"], f"Vidas: {datos['vida']}", (25, 15), FUENTE_RESPUESTA, COLOR_NEGRO)
        #en la pantalla ***
        mostrar_texto(pantalla, f"Tiempo: {tiempo_restante}s", (10, 470), FUENTE_TIEMPO, COLOR_NEGRO)
        mostrar_texto(pantalla, f"Puntaje: {datos['puntaje']}", (340, 5), FUENTE_TEXTO, COLOR_NEGRO)
        
        #boton_bomba = crear_elemento_juego("bomba.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 40, 250)
        #boton_x2 = crear_elemento_juego("x2.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 400, 250)
        #boton_doble = crear_elemento_juego("doble.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 400, 350)
        #boton_pasar = crear_elemento_juego("pasar.png", ANCHO_BOTON_COMODIN, ALTO_BOTON_COMODIN, 40, 350)
        if bandera_bomba:
            mostrar_texto(pantalla, "BOMBA",(30,230), FUENTE_RANKING,COLOR_VERDE_OSCURO)
        else:
            mostrar_texto(pantalla, "BOMBA",(30,230), FUENTE_RANKING,COLOR_ROJO_OSCURO)
            
        if bandera_x2:
            mostrar_texto(pantalla, "X2",(400,230), FUENTE_RANKING,COLOR_VERDE_OSCURO)
        else:
            mostrar_texto(pantalla, "X2",(400,230), FUENTE_RANKING,COLOR_ROJO_OSCURO)
        
        if bandera_doble:
            mostrar_texto(pantalla, "ESCUDO",(390,330), FUENTE_RANKING,COLOR_VERDE_OSCURO)
        else:
            mostrar_texto(pantalla, "ESCUDO",(390,330), FUENTE_RANKING,COLOR_ROJO_OSCURO)
            
        if bandera_pasar:
            mostrar_texto(pantalla, "SALTEAR",(25,330), FUENTE_RESPUESTA,COLOR_VERDE_OSCURO)
        else:
            mostrar_texto(pantalla, "SALTEAR",(25,330), FUENTE_RANKING,COLOR_ROJO_OSCURO)    
        pygame.display.flip()

    return "fin"

def guardar_partida(pantalla: pygame.Surface, puntaje):
    nombre = ""
    reloj = pygame.time.Clock()
    activo = True
    #creamos boton
    boton_retry = crear_elemento_juego("retry.png", ALTO_MINI_BOTON, ANCHO_MINI_BOTON, 230, 400)
    while activo:
        pantalla.blit(fondo_pantalla, (0, 0))
        pantalla.blit(boton_mini_menu["superficie"], boton_mini_menu["rectangulo"])
        pantalla.blit(boton_retry["superficie"], boton_retry["rectangulo"])
        
        mostrar_texto(pantalla, "¡Fin del juego!", (120, 50), FUENTE_GRANDE, COLOR_ROJO)
        mostrar_texto(pantalla, "Ingresá tu nombre (solo letras, máx 10)", (40, 150), FUENTE_TEXTO, COLOR_BLANCO)
        mostrar_texto(pantalla, nombre, (150, 220), FUENTE_TEXTO, COLOR_NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if boton_retry["rectangulo"].collidepoint(evento.pos):
                        reiniciar_datos()
                        return "jugar"
                    if boton_mini_menu["rectangulo"].collidepoint(evento.pos):
                        return "menu"
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if nombre.isalpha() and 1 <= len(nombre) <= 10:
                        guardar_en_json(nombre, puntaje)
                        return "menu"  
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    letra = evento.unicode
                    if letra.isalpha() and len(nombre) < 10:
                        nombre += letra

        pygame.display.flip()
        reloj.tick(FPS)