"""
Este modulo guardara toda la logica de
actualizacion de pantalla, deteccion de colisiones
y cosas relacionada a la logica del juego
"""

import pygame as pg
import math
from enemy import enemigos

pg.init()


# Clase para el disparo
class Disparo:

    def __init__(self, img, pantalla):
        """
        Esta clase contiene metodos para el monitoreo
        del disparo y su colisión
        """
        self.x = 380
        self.y = 550
        self.velocidad_x = 0
        self.velocidad_y = 10
        self.visible = False
        self.img = img
        self.pantalla = pantalla
        self.explosion = pg.image.load('assets/img/explosion.png')
        self.puntaje = 0

    # Detección del evento espacio

    def evento_espacio(self, event, x, y, pantalla, img):
        """
        Esta funcion se encarga de procesar el evento que se necesita
        """
        # Funcion para detectar tecla
        if event.type == pg.KEYDOWN:
            # Detectar si disparo continua en batalla
            if self.visible:
                # Reinicar visibilidad
                if self.y <= -64:
                    self.visible = False
                    self.y = 550  # Vuelve a la posición incial
                    self.x = 380
            # Generar disparo
            elif event.key == pg.K_z:
                # Cargar sonido de disparo
                sonido = pg.mixer.Sound('assets/sounds/disparo.mp3')
                sonido.set_volume(0.1)
                sonido.play()
                self.x = x
                self.y = y
                self.visible = True  # Cambiar estado de bala
                disparar_bala(self.x, self.y, self.pantalla, self.img)

    # Detectar colisión
    def detecto_colision(self, d_colision, enemigo):
        """
        Esta funcion hace que el disparo sea invisible
        despues de golpear al enemigo, que vuelva a la posición
        inicial y luego aumenta en 1 el puntaje
        """
        if d_colision:
            enemigo.sound.play()
            enemigo.sound.set_volume(0.3)
            self.visible = False
            self.d_explosion()
            self.y = 550  # Vuelve a la posición incial
            self.puntaje += 1


    def d_explosion(self):
        """
        Esta funcion se encarga de mostrar la explosion en pantalla
        """
        self.pantalla.blit(self.explosion, (self.x, self.y))


# Disparar
def disparar_bala(x, y, pantalla, img):
    """
    Esta funcino permite aparecer a la bala
    """

    # Hacemos que apareza en pantalla un poco corrido
    pantalla.blit(img, (x + 10, y + 10))


# Detectar colisiones
def valida_colision (x1, y1, x2, y2):
    """
    Esta funcion calcula la distancia entre el disparo
    y el enemigo, retorna un True al impactar
    """
    distancia = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    if distancia <= 27:
        colision = True
    else:
        colision = False
    return colision







