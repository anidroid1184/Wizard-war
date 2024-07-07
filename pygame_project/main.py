"""
Este modulo contiene el loop principal del juego
"""

import player
import enemy
import settings
import game
import pygame as pg


# Inicializar Pygame
pg.init()

# Pantalla

# Inicializar pantalla
pantalla = settings.crear_pantalla(800,600)

# Agregar titulo e icono a ventana del juego
settings.crear_titulo_iconos()

# Fondo de juego
fondo = settings.cargar_fondo()
scale_fondo = pg.transform.scale(fondo, (800, 600))

# Objetos

# Inicialización de jugador
jugador = player.jugador

# Inicialización de enemigos
enemigos = enemy.enemigos

# Inicializamos el disparo del jugador
dplayer = game.Disparo(pg.image.load('assets/img/disparo_player.png'), pantalla)

# Control de aplicación

# Iniciamos un reloj que manejara los FPS del juego
clock = pg.time.Clock()

# Intervalo para validar si una tecla se mantiene sostenida
pg.key.set_repeat(1, 25)

# Puntaje del jugador

puntaje = dplayer.puntaje
rtexto = settings.r_texto

# Loop del juego
ejecucion = True

# Cargar musica de fondo
settings.cargar_musica_fondo()
while ejecucion:
    """
    Este es el ciclo principal del juego
    """
    clock.tick(60)  # FPS
    pantalla.blit(scale_fondo, (0, 0))

    # Mostrar puntaje

    rtexto.mostrar_puntaje(dplayer.puntaje, pantalla)
    # Detección de eventos

    for evento in pg.event.get():

        # Cerrar juego
        if evento.type == pg.QUIT:
            ejecucion = False

        # Teclas presionadas

        # Movimiento de jugador
        jugador.x, jugador.y = player.movimiento(evento)

        # Movimienot de bala
        dplayer.evento_espacio(evento, jugador.x, jugador.y, pantalla, dplayer.img)

    # Tiempo en pantalla del disparo
    if dplayer.visible:
        game.disparar_bala(dplayer.x, dplayer.y, dplayer.pantalla, dplayer.img)
        dplayer.y -= dplayer.velocidad_y

    # mostrar los enemigos en pantalla
    for enemigo in enemigos:
        enemigo.x, enemigo.y = enemigo.movimiento()

    # Cargamos posiciones de los objetos

    jugador.posicion_jugador(pantalla)
    for enemigo in enemigos:
        enemigo.posicion_enemigo(pantalla)

    # Detectar colision
    for enemigo in enemigos:
        # Validar si algun enemigo está siendo golpeado
        colision = game.valida_colision(enemigo.x, enemigo.y, dplayer.x, dplayer.y)
        dplayer.detecto_colision(colision, enemigo)
        enemigo.aumentar_velocidad(colision)

    if dplayer.puntaje >= 30:
        rtexto.terminar_juego(pantalla)

    # actualizar pantalla
    pg.display.update()

