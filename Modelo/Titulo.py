class Titulo:
    def __init__(self, view_width, view_heigth, font, title, posicionx, posiciony):
        self.view_width = view_width
        self.view_heigth = view_heigth
        self.font = font
        self.title = title
        self.posicionx = self.view_width*posicionx
        self.posiciony= self.view_heigth*posiciony

    def draw(self, bg):
        msg = self.font.render(str(self.title), True, (255, 0, 0))
        bg.blit(msg, (self.posicionx,self.posiciony))