import pygame
class Window:

    def __init__(self, screen, hedge, frutita, pic, score):
        self.hog = hedge
        self.fruit = frutita
        self.image = pic
        self.score = score


        self.win = screen
        self.color = (0,0,0)


    def clean(self):
        self.win.fill(self.color)

    def draw(self, bg):
        bg.blit(self.image, (0,0))
        self.fruit.draw(self.win)
        self.hog.draw(self.win)
        self.score.draw(self.win)
        pygame.display.flip()
