import pygame
class Node(object):

    def __init__(self,  sprite, x, y, data=None, next_node=None):
        self.data = data
        self.prev = None
        self.next = next_node
        self.sprite = sprite
        self.x = x
        self.y = y

    def add_next(self, node):
        self.next = node
        node.prev = self
    def draw(self, bg):
        bg.blit(self.sprite, (int(self.x), int(self.y)))

#    def get_data(self):
#        return self.data

#    def get_next(self):
#        return self.next_node

#    def get_previous(self):