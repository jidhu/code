class Node:
    def __init__(self):                     # constructor
        self.data = None
        self.next = None
    def set_data(self, data):            #method for setting the data field of the Node
        self.data = data
    def get_data(self,data):            #method for getting the data field of the Node
        return self.data
    def set_next(self,next):            #method for setting the next field of the Node
        self.next = next
    def get_next(self,next):            #method for getting the next field of the Node
        return self.next
    def has_next(self):                   #returns true if the node points to another Node
        return self.next != None

a = Node()
b = Node()
