class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self,next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

head = Node()
ll1 = Node()
ll2 = Node()
head.set_data(7)
head.set_next(ll1)
ll1.set_data(6)
ll1.set_next(ll2)
ll2.set_data(5)
ll1 = Node()
ll2.set_next(ll1)
ll1.set_data(4)
ll2 = Node()
ll1.set_next(head)

del ll1
del ll2
