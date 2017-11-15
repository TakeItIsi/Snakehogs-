class Puntaje:
        def __init__(self, view_width, font):
            # type: (object, object) -> object
            self.view_width = view_width
            self.font = font
            self.counter = 0

        def draw(self, bg):
            msg = self.font.render(str(self.counter), True, (0, 0, 0))
            bg.blit(msg, (self.view_width-36, 0))

        def add(self):
            self.counter += 1