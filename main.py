#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
from Controlador.Basic_Controller import Controlador
from Controlador.Menu_Controller import Menu
from Controlador.Versus_Controller import Versus_Controlador

__author__ = "Isidora Ulloa"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "isidora.ulloa@ug.uchile.cl"

pygame.init()
titulo = Menu("Recursos/menu sprite full.png","", True)
while True:
    while titulo.mainloop:
        titulo.run()
    if titulo.versus.on:
        instruccion = Menu("Recursos/instrucciones 12.png","", False)
        program = Versus_Controlador(titulo.walls.on)
    else:
        instruccion = Menu("Recursos/instrucciones 11.png", "", False)
        program = Controlador(titulo.walls.on)
    while  instruccion.mainloop:
        instruccion.run()
    while program.run==True:
        program.update()
        pygame.time.wait(program.refresh)
    if titulo.versus.on:
        fin = Menu(program.end,"Cuy: " + str(program.puntaje2.counter) + "                            Erizo: " + str(program.puntaje1.counter), False)
    else:
        fin= Menu(program.end, "                 Puntos: " + str(program.puntaje.counter), False)
    while fin.running==True:
        fin.run()
    titulo.mainloop=True

