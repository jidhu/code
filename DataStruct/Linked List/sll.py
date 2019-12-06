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

ll = Node()
ll2 = Node()
ll.set_data(5)
print(ll.get_data())
ll.set_next(ll2)
print(ll2.get_next())

print(ll.has_next())
print(ll2.has_next())