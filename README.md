# 🧙 Wizards Pygame

**Wizards** es un juego arcade desarrollado con **Pygame**, en el que controlas a un mago que debe esquivar enemigos y lanzar hechizos para sobrevivir. Inspirado en los clásicos juegos de naves, el jugador se mueve horizontalmente, disparando proyectiles mágicos mientras evita ataques enemigos.

---

## 🎮 Características

- Movimiento horizontal del jugador (estilo *shooter horizontal clásico*).
- Sistema de enemigos con lógica de aparición y movimiento.
- Módulo de colisiones y detección de impactos.
- Modularización completa en múltiples archivos (`main.py`, `player.py`, `enemy.py`, etc.).
- Soporte para múltiples fuentes personalizadas (`Magic Wand.ttf`, `Wizards' Magic.ttf`).
- Configuración centralizada de constantes y variables en `settings.py`.
- Carpeta `assets/` para gestionar recursos gráficos y/o sonoros.
- Compatible con Python 3 y Pygame.

"""
## 🗂 Estructura del Proyecto

Wizards/<br>
├── assets/                # Recursos gráficos y sonoros 
├── __pycache__/           # Archivos temporales (ignorar)
├── Magic Wand.ttf         # Fuente mágica
├── Wizards' Magic.ttf     # Fuente decorativa
├── __init__.py            # Inicialización del paquete
├── enemy.py               # Lógica de los enemigos
├── game.py                # Gestión del ciclo principal del juego
├── main.py                # Punto de entrada del juego
├── player.py              # Control y lógica del jugador
├── settings.py            # Variables globales de configuración

---

## 🛠 Instalación y ejecución

### Requisitos

- Python 3.8 o superior
- Pygame (`pip install pygame`)

### Ejecutar el juego

```
python main.py
```

## 🧩 Modularización
El proyecto está dividido en módulos para mantener el código limpio y fácil de escalar:

main.py: Inicializa y ejecuta el juego.

game.py: Lógica del ciclo de juego (renderizado, actualización, eventos).

player.py: Clase y comportamiento del jugador.

enemy.py: Generación y movimiento de enemigos.

settings.py: Configuraciones generales (tamaño de pantalla, colores, FPS, etc.).

## 📄 Licencia
Este proyecto es de código abierto bajo los términos de la licencia MIT.

## ✨ Créditos
Desarrollado por anidroid1184
