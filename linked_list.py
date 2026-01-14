class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def pop(self):
        temp = self.head
        pre = self.head
        if self.length == 0:
            print("The list is Empty. Please add items to the list!!")
            return None
        elif self.length ==1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length +=1
        return True

    def popfirst(self):
        temp = self.head
        if self.length == 0:
            print("The list is Empty. Please add items to the list!!")
            return None
        elif self.length ==1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            self.head = self.head.next
            self.length -= 1
            return temp.value
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        node = self.get(index)
        if node is None:
            return None
        node.value = value
        return node
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length -1:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        self.length -= 1
        return temp.value
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None:
            fast = fast.next.next 
            slow = slow.next
            return slow

        



        

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)




# #get
# print(my_linked_list.get(2).value)

#set
#print(my_linked_list.set_value(2, 69).value)

#insert
# print(my_linked_list.insert(2, 69))

#remove
# print(my_linked_list.remove(2))

#reverse
my_linked_list.reverse()

# my_linked_list.prepend(8)

# print("\nPopped value:")
# print(my_linked_list.pop()) 

# print("\nPopped value:")
# print(my_linked_list.popfirst()) 

print("\nList after pop:")
my_linked_list.print_list()


