class Node:
    def __init__(self,y,x):
        self.data = x
        self.next = y
    
head = Node(None,5)
obj = Node(head,4)
obj = Node(obj,3)
obj = Node(obj,2)
obj = Node(obj,1)
