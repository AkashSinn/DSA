class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return new_node
    

    def pop(self):
        temp = self.tail
        if self.length == 0:
            print ("No node is in the list")
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return temp.value
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -=1
            return temp.value
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
        return new_node
    
    def popfirst(self):
        temp = self.head
        if self.length == 0:
            print ("No node is in the list")
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return temp.value
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -=1
            return temp.value
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None