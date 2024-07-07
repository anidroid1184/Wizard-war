"""
Este modulo guarda la clase enemy
que guadara la actualización de estado
del self
"""


import pygame as pg
from random import randint as rd

pg.init()


class Enemy:

    def __init__(self, img, sound):
        self.x = rd(0, 736) # Posicion inicial x
        self.y = rd(64, 536) # Posicion inicial y
        self.cambio_pos_x = 0
        self.cambio_pos_y = 0
        self.velocidad = 0.8
        self.img = img
        self.sound = sound

    # Funcion para mostrar al enemigo en pantalla
    def posicion_enemigo(self, pantalla):
        pantalla.blit(self.img, (self.x, self.y))

    # Funcion de movimiento aleatorio
    def movimiento(self):
        # Comprobar que no se salga de los limites
        self.x += self.velocidad

        # Movimineto horizontal
        if self.x >= 736:
            self.cambio_pos_x -= self.velocidad
            self.cambio_pos_y = -self.velocidad

        if self.x <= 0:
            self.cambio_pos_x += self.velocidad
            self.cambio_pos_y = -self.velocidad

        # Movimiento vertical
        if self.y >= 536:
            self.cambio_pos_y -= self.velocidad
        elif self.y <= 64:
            self.cambio_pos_y += self.velocidad

        self.x += self.cambio_pos_x
        self.y += self.cambio_pos_y

        return self.x, self.y

    def aumentar_velocidad(self, colision):
        if colision:
            self.velocidad += 0.8


# Variable enemigos
enemigo1 = Enemy(
    pg.image.load("assets/img/enemy.png"),
    pg.mixer.Sound("assets/sounds/golpeo_mago.mp3"),
)
enemigo2 = Enemy(
    pg.image.load("assets/img/enemy2.png"),
    pg.mixer.Sound("assets/sounds/golpear_dragon.mp3")
)
enemigo3 = Enemy(
    pg.image.load("assets/img/enemy3.png"),
    pg.mixer.Sound("assets/sounds/golpear_calabera.mp3")
)
enemigo4 = Enemy(
    pg.image.load("assets/img/enemy4.png"),
    pg.mixer.Sound("assets/sounds/golpear_pulpo.mp3")
)

# Lista para el manejo de enemigos
enemigos = [enemigo1,
            enemigo2,
            enemigo3,
            enemigo4
]
