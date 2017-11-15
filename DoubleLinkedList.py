from Nodo import Node
class DList:
    def __init__(self):
        self.head=Node()
        self.tail=self.head
    def add_to_tail(self, node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node