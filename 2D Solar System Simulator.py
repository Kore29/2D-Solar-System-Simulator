'''
Descripción
El objetivo de este proyecto es crear una simulación simplificada de un sistema solar en dos dimensiones. En esta simulación, deberás representar el Sol y varios planetas orbitando a su alrededor. Los planetas deberán seguir trayectorias elípticas y sus velocidades deberán ajustarse de acuerdo a las leyes de Kepler.

Requisitos
1. Visualización: Usar una librería como pygame o matplotlib para visualizar el sistema solar.
2. Física: Implementar las leyes de Kepler para calcular las órbitas y velocidades de los planetas.
3. Interactividad: Permitir que el usuario pueda añadir, eliminar o modificar planetas y sus órbitas.
'''

import pygame
import matplotlib

pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Prueba')

# Inicio
runing = True
while runing:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            runing = False

