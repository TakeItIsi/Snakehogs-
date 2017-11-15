import pygame
class Versus_Window:

    def __init__(self, screen, hedge, cuy, frutita, pic, score1, score2):
        self.hog = hedge
        self.cuy = cuy
        self.fruit = frutita
        self.image = pic
        self.score1 = score1
        self.score2 = score2


        self.win = screen
        self.color = (0,0,0)


    def clean(self):
        self.win.fill(self.color)

    def draw(self, bg):
        bg.blit(self.image, (0,0))
        self.fruit.draw(self.win)
        self.hog.draw(self.win)
        self.cuy.draw(self.win)
        self.score1.draw(self.win)
        self.score2.draw(self.win)
        pygame.display.flip()
