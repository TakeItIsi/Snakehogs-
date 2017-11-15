from Nodo import Node
class Snedgehog:
    def __init__(self, initial_x, initial_y, speed, front1,front2,back1,back2,left1,left2,right1,right2):
        self.x = initial_x
        self.y = initial_y
        self.speed= speed
        self.speedx = speed
        self.speedy = 0


        #Sprites
        self.spritefront1 = front1
        self.spritefront2 = front2
        self.spriteback1 = back1
        self.spriteback2 = back2
        self.spriteleft1 = left1
        self.spriteleft2 = left2
        self.spriteright1 = right1
        self.spriteright2 = right2
        self.sprite = right1

        self.head = Node(self.sprite, self.x, self.y)
        self.tail = self.head

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def omnomnom(self):

        newErizo = Node(self.head.sprite, 0, 0)
        newErizo.prev = self.tail
        self.tail.next = newErizo
        self.tail = newErizo

    #moviending al snedgehog
    def chocar(self):
        if self.tail is not self.head:
            aux = self.tail
            while aux.prev is not self.head:
                if aux.x == self.head.x and aux.y == self.head.y:
                    return True
                    break
                else:
                    aux = aux.prev


    def upd8(self):
        aux = self.tail
        while aux.prev is not None:

                aux.x = int(aux.prev.x)
                aux.y = int(aux.prev.y)
                aux.sprite= aux.prev.sprite
                aux = aux.prev

        self.head.x += self.speedx
        self.head.y += self.speedy
        if self.speedx > 0:
            if (int(self.head.x)!= 0) and (int(self.head.x)%2*self.speed)==0:
                self.sprite = self.spriteright1
            elif (int(self.head.x) == 0):
                self.sprite = self.spriteright1
            else:
                self.sprite = self.spriteright2
        elif self.speedx < 0:
            if (int(self.head.x)!= 0) and (int(self.head.x)%2*self.speed)==0:
                self.sprite = self.spriteleft1
            elif (int(self.head.x)==0):
                self.sprite = self.spriteleft1
            else:
                self.sprite = self.spriteleft2
        elif self.speedy > 0:
            if (int(self.head.y)!=0) and (int(self.head.y)%2*self.speed)==0:
                self.sprite = self.spritefront1
            elif (int(self.head.y)==0):
                self.sprite = self.spritefront1
            else:
                self.sprite = self.spritefront2
        elif self.speedy < 0:
            if (int(self.head.y) !=0) and (int(self.head.y)%2*self.speed)==0:
                self.sprite = self.spriteback1
            elif (int(self.head.y)==0):
                self.sprite = self.spriteback1
            else:
                self.sprite = self.spriteback2
        self.head.sprite=self.sprite

    def draw(self, bg):
        aux = self.tail
        while aux is not None:
            aux.draw(bg)
            aux=aux.prev