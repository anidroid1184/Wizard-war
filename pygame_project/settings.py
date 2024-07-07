"""
Este modulo guarda las configuraciones
generales del proyecto
"""
import pygame as pg
from pygame import mixer
import io
pg.init()


class Puntaje:

    def __init__(self):
        self.x = 0
        self.y = -32
        self.fuente1, self.fuente2 = self.asignar_fuentes()

    def asignar_fuentes(self):
       fuente_byte1 = self.fuente1_bytes('Magic Wand.ttf')
       fuente_byte2 = self.fuente2_bytes('Magic Wand.ttf')
       fuente1 = pg.font.Font(fuente_byte1, 32)
       fuente2 = pg.font.Font(fuente_byte2, 80)
       return fuente1, fuente2

    def fuente1_bytes(self,fuente1):
        with open(fuente1, 'rb') as f:
            ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

    def fuente2_bytes(self, fuente2):
        with open(fuente2, 'rb') as f:
            ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

    def mostrar_puntaje(self, puntaje, pantalla):
        """
        Esta funcion se encargara de mostrar el puntaje del jugador
        """
        texto = self.fuente1.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
        pantalla.blit(texto, (self.x, self.y))

    def terminar_juego(self, pantalla):
        texto = self.fuente2.render(f'HAS GANADO', True, (255, 255, 255), (0, 0, 0))
        pantalla.blit(texto, (60, 200))






# Variable para renderizar texto
r_texto = Puntaje()

def crear_pantalla(x,y):
    """
    Esta funcion  crea y asigna el tamaño de la pantalla
    """
    screen = pg.display.set_mode((x, y))
    return screen


def crear_titulo_iconos():
    """
    Esta función asigna el tutlo de la ventana y también su icono
    """
    pg.display.set_caption("Wizards war")
    icono = pg.image.load('assets/img/icon.png')
    pg.display.set_icon(icono)


def cargar_fondo():
    """
    Esta función se encarga de asignar la imagen pasada como argumento como
    fondo para el juego
    """
    fondo = pg.image.load('assets/img/background.jpg')
    return fondo


def cargar_musica_fondo():
    """
    Este modulo carga la musica de fondo
    """
    mixer.music.load('assets/sounds/musica_fondo.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)



