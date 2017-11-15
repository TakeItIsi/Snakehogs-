class Switch:
    def __init__(self, x, y, on_image, off_image):
        self.x = x
        self.y = y
        self.on_image = on_image
        self.off_image = off_image
        self.image = self.off_image
        self.on = False
        self.off = True
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_on(self):
        return self.on
    def get_bound_x(self):
        return self.image.get_size()[0] + self.x
    def get_bound_y(self):
        return self.image.get_size()[1] + self.y
    def switched(self):
        if self.on == True:
            self.on = False
            self.off = True
            self.image = self.off_image
        elif self.off == True:
            self.off = False
            self.on = True
            self.image = self.on_image
    def draw(self,bg):
        bg.blit(self.image, (int(self.x), int(self.y)))