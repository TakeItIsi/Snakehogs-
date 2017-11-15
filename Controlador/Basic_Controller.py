import os
import random
import pygame
import sys

from Modelo.Snedgehog import Snedgehog
from Modelo.Fruta import Fruta
from Vista.Window import Window
from Modelo.Puntos import Puntaje

pygame.init()

class Controlador:
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
        self.end = "Recursos/game over 1.png"

        pygame.display.set_caption('Hedgehogs')
#SPRITES
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
#FRUTAS
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
#ESPECIALES
        self.coffe_image = pygame.image.load(os.path.join("Recursos/frutas/cafecito.png"))
        self.coffe_image.convert_alpha() #VELOCIDAD X2
        self.tea_image = pygame.image.load(os.path.join("Recursos/frutas/tecito.png"))
        self.tea_image.convert_alpha() #VELOCIDAD /2
#FONDOS
        fondo_image_redondo = pygame.image.load(os.path.join("Recursos/fondo 2x2.png"))
        fondo_image_redondo.convert_alpha()
        fondo_image_pared = pygame.image.load(os.path.join("Recursos/fondo pared.png"))
        fondo_image_pared.convert_alpha()
#MODELOS
        self.erizo = Snedgehog(36,36, 36, front1_image,front2_image,back1_image,back2_image,left1_image,left2_image,right1_image,right2_image)
        self.frutita = Fruta(random.randint(1, 7) * 36, random.randint(1, 7) * 36, (random.choice(self.frutitas)))
        self.puntaje = Puntaje(self.width, self.font)
        if self.paredes:
            self.window = Window(self.win, self.erizo, self.frutita, fondo_image_pared, self.puntaje)
        else:
            self.window = Window(self.win, self.erizo, self.frutita, fondo_image_redondo, self.puntaje)
#SONIDOS
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
        else:
#EL MUNDO ES CUADRADO
            if (int(self.erizo.head.x)>=self.width-36) or (int(self.erizo.head.x)<0+36) or (int(self.erizo.head.y)>=self.height-36) or (int(self.erizo.head.y)<0+36):
                self.run = False
#MOVERSE (known bugs: si se aprietan dos botones en un mismo ciclo de refresh puede hacer cosas imposibles como devolverse
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
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
#SALIR
                if event.key == pygame.K_ESCAPE:
                    self.run = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#COMER
        if int(self.erizo.head.x)==self.frutita.get_x() and int(self.erizo.head.y)==self.frutita.get_y():
            self.puntaje.add()
            self.crunch.play()
            if self.frutita.sprite==self.coffe_image:
                self.refresh = self.refresh*3/4
            elif self.frutita.sprite == self.tea_image:
                self.refresh = self.refresh*5/4
            self.frutita.x = random.randint(1, 7) * 36
            self.frutita.y = random.randint(1, 7) * 36
            aux = self.erizo.tail
            while aux.prev is not None:
                if aux.x == self.frutita.x and aux.y == self.frutita.y:
                    self.frutita.x = random.randint(1, 7) * 36
                    self.frutita.y = random.randint(1, 7) * 36
                    aux = self.erizo.tail
                else:
                    aux = aux.prev
            ran = random.randint(0,100)
            if ran<10:
                self.frutita.sprite=self.coffe_image
            elif ran <20 and ran >=10:
                self.frutita.sprite = self.tea_image
            else:
                self.frutita.sprite = random.choice(self.frutitas)
            self.erizo.omnomnom()
#CHOCARRRRRR
        if self.erizo.chocar():
            self.run = False
        self.erizo.upd8()