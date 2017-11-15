import os
import random

import pygame
import sys

from Modelo.Snedgehog import Snedgehog
from Modelo.Fruta import Fruta
from Vista.Window import Window
from Vista.Versus_Window import Versus_Window
from Modelo.Puntos import Puntaje

pygame.init()

class Versus_Controlador:
    def __init__(self, hay_paredes):
        pygame.init()
        self.height = 36*10
        self.width = 36*10
        self.frutitas = []
        self.paredes = hay_paredes
        self.font = pygame.font.SysFont("Arial", 25)
        self.run = True
        self.refresh = 1000/7
        self.win = pygame.display.set_mode([self.width, self.height])
        self.end = "Recursos/game over 2.png"
        pygame.display.set_caption('Hedgehogs')
#SPRITES: ERIZO
        back1_image = pygame.image.load(os.path.join("Recursos/hogitos/back 11.png"))
        back1_image.convert_alpha()
        back2_image = pygame.image.load(os.path.join("Recursos/hogitos/back 22.png"))
        back2_image.convert_alpha()
        front1_image = pygame.image.load(os.path.join("Recursos/hogitos/front 11.png"))
        front1_image.convert_alpha()
        front2_image = pygame.image.load(os.path.join("Recursos/hogitos/front 22.png"))
        front2_image.convert_alpha()
        left1_image = pygame.image.load(os.path.join("Recursos/hogitos/left 11.png"))
        left1_image.convert_alpha()
        left2_image = pygame.image.load(os.path.join("Recursos/hogitos/left 22.png"))
        left2_image.convert_alpha()
        right1_image = pygame.image.load(os.path.join("Recursos/hogitos/right 11.png"))
        right1_image.convert_alpha()
        right2_image = pygame.image.load(os.path.join("Recursos/hogitos/right 22.png"))
        right2_image.convert_alpha()
#SPRITES: CUY
        cback1_image = pygame.image.load(os.path.join("Recursos/hogitos/back 1.png"))
        cback1_image.convert_alpha()
        cback2_image = pygame.image.load(os.path.join("Recursos/hogitos/back 2.png"))
        cback2_image.convert_alpha()
        cfront1_image = pygame.image.load(os.path.join("Recursos/hogitos/front 1.png"))
        cfront1_image.convert_alpha()
        cfront2_image = pygame.image.load(os.path.join("Recursos/hogitos/front 2.png"))
        cfront2_image.convert_alpha()
        cleft1_image = pygame.image.load(os.path.join("Recursos/hogitos/left 1.png"))
        cleft1_image.convert_alpha()
        cleft2_image = pygame.image.load(os.path.join("Recursos/hogitos/left 2.png"))
        cleft2_image.convert_alpha()
        cright1_image = pygame.image.load(os.path.join("Recursos/hogitos/right 1.png"))
        cright1_image.convert_alpha()
        cright2_image = pygame.image.load(os.path.join("Recursos/hogitos/right 2.png"))
        cright2_image.convert_alpha()
#FRUTAS (Notese que en este modo no hay te o cafe para no complicarle la vida al mundo)
        lila_image = pygame.image.load(os.path.join("Recursos/frutas/fruta manzana.png"))
        lila_image.convert_alpha()
        self.frutitas.append(lila_image)
        naranja_image = pygame.image.load(os.path.join("Recursos/frutas/fruta naranjita.png"))
        naranja_image.convert_alpha()
        self.frutitas.append(naranja_image)
        roja_image = pygame.image.load(os.path.join("Recursos/frutas/fruta frutilla.png"))
        roja_image.convert_alpha()
        self.frutitas.append(roja_image)
        verde_image = pygame.image.load(os.path.join("Recursos/frutas/fruta kiwi.png"))
        verde_image.convert_alpha()
        self.frutitas.append(verde_image)
        azul_image = pygame.image.load(os.path.join("Recursos/frutas/fruta arandano.png"))
        azul_image.convert_alpha()
        self.frutitas.append(azul_image)
        amarillo_image = pygame.image.load(os.path.join("Recursos/frutas/fruta platano.png"))
        amarillo_image.convert_alpha()
        self.frutitas.append(amarillo_image)
#FONDOS
        fondo_image_redondo = pygame.image.load(os.path.join("Recursos/fondo 2x2.png"))
        fondo_image_redondo.convert_alpha()
        fondo_image_pared = pygame.image.load(os.path.join("Recursos/fondo pared.png"))
        fondo_image_pared.convert_alpha()
#MODELOS
        self.erizo = Snedgehog(36,36, 36, front1_image,front2_image,back1_image,back2_image,left1_image,left2_image,right1_image,right2_image)
        self.cuy = Snedgehog(36, self.height-72, 36, cfront1_image, cfront2_image, cback1_image, cback2_image, cleft1_image, cleft2_image, cright1_image, cright2_image)
        self.frutita = Fruta(random.randint(1, 7) * 36, random.randint(1, 7) * 36, (random.choice(self.frutitas)))
        self.puntaje1 = Puntaje(self.width, self.font)
        self.puntaje2 = Puntaje(72, self.font)
        if self.paredes:
            self.window = Versus_Window(self.win, self.erizo, self.cuy, self.frutita, fondo_image_pared, self.puntaje1, self.puntaje2)
        else:
            self.window = Versus_Window(self.win, self.erizo, self.cuy, self.frutita, fondo_image_redondo, self.puntaje1, self.puntaje2)

        #musica de fondo: Fortree City by Go Ichinose for Pokemon Ruby & Sapphire
        pygame.mixer.music.load("Recursos/fondooo.wav")
        pygame.mixer.music.play(-1, 0.0)
        #crunch sound creditos a https://freesound.org/people/xtrgamr/sounds/253619/
        self.crunch = pygame.mixer.Sound("Recursos/crunchy.wav")
        self.crunch.set_volume(10)

    def update(self):
        self.window.clean()
        self.window.draw(self.win)
        # EL MUNDO ES REDONDO
        if self.paredes==False:
            if (int(self.erizo.head.x)>=self.width):
                    self.erizo.head.x=0
            if (int(self.erizo.head.x)<0):
                    self.erizo.head.x=self.width
            if (int(self.erizo.head.y)>=self.height):
                    self.erizo.head.y=0
            if (int(self.erizo.head.y)<0):
                    self.erizo.head.y=self.height

            if (int(self.cuy.head.x) >= self.width):
                self.cuy.head.x = 0
            if (int(self.cuy.head.x) < 0):
                self.cuy.head.x = self.width
            if (int(self.cuy.head.y) >= self.height):
                self.cuy.head.y = 0
            if (int(self.cuy.head.y) < 0):
                self.cuy.head.y = self.height

        else:
            if ((int(self.erizo.head.x)>=self.width-36) or (int(self.erizo.head.x)<0+36) or (int(self.erizo.head.y)>=self.height-36) or (int(self.erizo.head.y)<0+36)) and ((int(self.cuy.head.x) >= self.width - 36) or (int(self.cuy.head.x) < 0 + 36) or (int(self.cuy.head.y) >= self.height - 36) or (int(self.cuy.head.y) < 0 + 36)):
                self.end = "Recursos/game over 2.png"
                self.run = False
            elif (int(self.erizo.head.x)>=self.width-36) or (int(self.erizo.head.x)<0+36) or (int(self.erizo.head.y)>=self.height-36) or (int(self.erizo.head.y)<0+36):
                self.end = "Recursos/game over cuy.png"
                self.run = False
            elif (int(self.cuy.head.x) >= self.width - 36) or (int(self.cuy.head.x) < 0 + 36) or (int(self.cuy.head.y) >= self.height - 36) or (int(self.cuy.head.y) < 0 + 36):
                self.end = "Recursos/game over erizo.png"
                self.run = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
#MOVERSE
                if event.key == pygame.K_DOWN:
                    if self.erizo.speedy != -self.erizo.speed:
                        self.erizo.speedx = 0
                        self.erizo.speedy = self.erizo.speed
                if event.key == pygame.K_UP:
                    if self.erizo.speedy != self.erizo.speed:
                        self.erizo.speedx = 0
                        self.erizo.speedy = -self.erizo.speed
                if event.key == pygame.K_LEFT:
                    if self.erizo.speedx != self.erizo.speed:
                        self.erizo.speedy = 0
                        self.erizo.speedx = -self.erizo.speed
                if event.key == pygame.K_RIGHT:
                    if self.erizo.speedx != -self.erizo.speed:
                        self.erizo.speedy = 0
                        self.erizo.speedx = self.erizo.speed

                if event.key == pygame.K_s:
                    if self.cuy.speedy != -self.cuy.speed:
                        self.cuy.speedx = 0
                        self.cuy.speedy = self.cuy.speed
                if event.key == pygame.K_w:
                    if self.cuy.speedy != self.cuy.speed:
                        self.cuy.speedx = 0
                        self.cuy.speedy = -self.cuy.speed
                if event.key == pygame.K_a:
                    if self.cuy.speedx != self.cuy.speed:
                        self.cuy.speedy = 0
                        self.cuy.speedx = -self.cuy.speed
                if event.key == pygame.K_d:
                    if self.cuy.speedx != -self.cuy.speed:
                        self.cuy.speedy = 0
                        self.cuy.speedx = self.cuy.speed

                if event.key == pygame.K_ESCAPE:
                    self.run = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#COMER
        if int(self.erizo.head.x)==self.frutita.get_x() and int(self.erizo.head.y)==self.frutita.get_y():
            self.puntaje1.add()
            self.crunch.play()
            self.frutita.x = random.randint(1, 7) * 36
            self.frutita.y = random.randint(1, 7) * 36
            aux = self.erizo.tail
            while aux.prev is not None:
                if aux.x == self.frutita.x and aux.y==self.frutita.y:
                    self.frutita.x = random.randint(1, 7) * 36
                    self.frutita.y = random.randint(1, 7) * 36
                    aux = self.erizo.tail
                else:
                    aux = aux.prev
            self.frutita.sprite = random.choice(self.frutitas)
            self.erizo.omnomnom()

        elif int(self.cuy.head.x)==self.frutita.get_x() and int(self.cuy.head.y)==self.frutita.get_y():
            self.puntaje2.add()
            self.crunch.play()
            self.frutita.x = random.randint(1, 7) * 36
            self.frutita.y = random.randint(1, 7) * 36
            aux = self.cuy.tail
            while aux.prev is not None:
                if aux.x == self.frutita.x and aux.y==self.frutita.y:
                    self.frutita.x = random.randint(1, 7) * 36
                    self.frutita.y = random.randint(1, 7) * 36
                    aux = self.cuy.tail
                else:
                    aux =   aux.prev
            self.frutita.sprite = random.choice(self.frutitas)
            self.cuy.omnomnom()
#CHOCARRRRRR
        if self.erizo.chocar():
            self.end = "Recursos/game over cuy.png"
            self.run = False
        elif self.cuy.chocar():
            self.end = "Recursos/game over erizo.png"
            self.run = False
#CHOCAR ENTRE DOSSSS
        if self.erizo.head.x == self.cuy.head.x and self.erizo.head.y == self.cuy.head.y:
            self.end = "Recursos/game over 2.png"
            self.run = False
        if self.erizo.head.x==self.cuy.tail.x and self.erizo.head.y==self.cuy.tail.y:
            self.end = "Recursos/game over cuy.png"
            self.run = False
        if self.cuy.head.x == self.erizo.tail.x and self.cuy.head.y == self.erizo.tail.y:
            self.end = "Recursos/game over erizo.png"
            self.run = False
        if self.cuy.tail.x != self.cuy.head.x or self.cuy.tail.y != self.cuy.head.y:
            aux = self.cuy.tail
            while aux.prev is not None:
                if aux.x == self.erizo.head.x and aux.y == self.erizo.head.y:
                    self.end = "Recursos/game over cuy.png"
                    self.run = False
                    break
                else:
                    aux = aux.prev
        if self.erizo.tail.x != self.erizo.head.x or self.erizo.tail.y != self.erizo.head.y:
            aux = self.erizo.tail
            while aux.prev is not None:
                if aux.x == self.cuy.head.x and aux.y == self.cuy.head.y:
                    self.end = "Recursos/game over erizo.png"
                    self.run = False
                    break
                else:
                    aux = aux.prev

        self.erizo.upd8()
        self.cuy.upd8()