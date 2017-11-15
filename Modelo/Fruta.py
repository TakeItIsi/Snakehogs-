class Fruta:

    def __init__(self, x_pos, y_pos, image):
        self.x = x_pos
        self.y = y_pos
        self.validity = True
        self.impact = False
        self.sprite = image

    def set_validity(self, status):
        self.validity = status

    def is_valid(self):
        return self.validity

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self, bg):
        bg.blit(self.sprite, (int(self.x), int(self.y)))
