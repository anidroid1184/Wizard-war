"""
Este modulo define la clase jugador
que guardara la actualización de estado
"""
import pygame as pg

pg.init()


class Player:

    def __init__(self):
        self.x = 368  # Posicion inicial x
        self.y = 534  # Posicion inicial y
        self.cambio_pos_x = 0
        self.cambio_pos_y = 0
        self.velocidad = 5
        self.img = pg.image.load("assets/img/player.png")  # Imagen de jugador

    def posicion_jugador(self, pantalla):
        pantalla.blit(self.img, (self.x, self.y))


# iniciamos la variable con clase player
jugador = Player()


# Generar y verificar movimiento
def movimiento(evento):
    # Detectar si se presiono una tecla
    if evento.type == pg.KEYDOWN:

        # Tecla izquierda
        if evento.key == pg.K_LEFT:
            jugador.cambio_pos_x = -jugador.velocidad

        # Tecla derecha
        if evento.key == pg.K_RIGHT:
            jugador.cambio_pos_x = jugador.velocidad

        # Tecla arribla
        if evento.key == pg.K_UP:
            jugador.cambio_pos_y = -jugador.velocidad

        # Tecla abajo
        if evento.key == pg.K_DOWN:
            jugador.cambio_pos_y = jugador.velocidad

    # Detectar que la tecla se solto
    if evento.type == pg.KEYUP:
        # Reestablecer variables segun sea x o y
        if evento.key == pg.K_LEFT or evento.key == pg.K_RIGHT:
            jugador.cambio_pos_x = 0
        if evento.key == pg.K_UP or evento.key == pg.K_DOWN:
            jugador.cambio_pos_y = 0

    # Actualizamos posiciones
    jugador.x += jugador.cambio_pos_x
    jugador.y += jugador.cambio_pos_y

    # Comprobar que no se salga de los limites
    if jugador.x >= 736:
        jugador.x = 736

    if jugador.x <= 0:
        jugador.x = 0

        # Movimiento en Y

    if jugador.y >= 534:
        jugador.y = 534

    if jugador.y <= 384:
        jugador.y = 384

    return jugador.x, jugador.y


