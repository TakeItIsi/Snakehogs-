import os
import random

import pygame
import sys
import os
from Modelo.Titulo import Titulo
from Modelo.Boton import Switch
pygame.init()

class Menu:
    def __init__(self, fondo, subtitulo, draws):
        self.height = 36 * 10
        self.width = 36 * 10
        self.draws = draws
        self.redondo = True
        self.running = True
        self.font2 = pygame.font.SysFont("Impact", 20)
        self.win = pygame.display.set_mode([self.width, self.height])
        pygame.init()
#PUNTAJE
        self.subtitulo = Titulo (int(self.width), int(self.height), self.font2, str(subtitulo), 0.2, 0.1)
#FONDOS
        self.fondo_image = pygame.image.load(os.path.join("Recursos/fondo base.png"))
        self.fondo_image.convert_alpha()
        self.fondomenu = pygame.image.load(os.path.join(fondo)) #depende del estado del juego
        self.fondomenu.convert_alpha()
#BOTONES
        self.paredeson_image = pygame.image.load(os.path.join("Recursos/pared on.png"))
        self.paredeson_image.convert_alpha()
        self.paredesoff_image = pygame.image.load(os.path.join("Recursos/pared off.png"))
        self.paredesoff_image.convert_alpha()
        self.versuson_image = pygame.image.load(os.path.join("Recursos/versus on.png"))
        self.versuson_image.convert_alpha()
        self.versusoff_image = pygame.image.load(os.path.join("Recursos/versus off.png"))
        self.versusoff_image.convert_alpha()
        self.walls = Switch(self.width*0.2, self.height*0.8, self.paredeson_image, self.paredesoff_image)
        self.versus = Switch(self.width*0.6, self.height*0.8, self.versuson_image, self.versusoff_image)

        pygame.display.set_caption('Hedgehogs')
        self.mainloop = True

    def run(self):
            self.mainloop = True #siempre se define true
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = False
                        self.mainloop = False
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_pos[0] in range(int(self.walls.get_x()), int(self.walls.get_bound_x()), 1) and mouse_pos[1] in range(int(self.walls.get_y()), int(self.walls.get_bound_y()), 1):
                        self.walls.switched()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_pos[0] in range(int(self.versus.get_x()), int(self.versus.get_bound_x()), 1) and mouse_pos[1] in range(int(self.versus.get_y()), int(self.versus.get_bound_y()), 1):
                        self.versus.switched()
                if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

            self.win.blit(self.fondo_image, (0, 0))
            self.win.blit(self.fondomenu, (0, 0))
            #self.titulo.draw(self.win)
            self.subtitulo.draw(self.win)
            if self.draws:
                self.walls.draw(self.win)
                self.versus.draw(self.win)
            pygame.display.flip()