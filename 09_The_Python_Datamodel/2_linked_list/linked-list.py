class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.__dict__}'

# Validates the head parameter given in the initializer by calling the head property setter
class LinkedList:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        copied_list = []
        next = True
        current_node = self.head
        while next:
            if current_node.next != None:
                copied_list.append(current_node)
                current_node = current_node.next
            else:
                next = False
        return copied_list
            
        
    @property
    def head(self):
        return self._head
    @head.setter
    def head(self, value):
        if type(value) == Node:
            self._head = value
        else: raise TypeError('The type should be Node')

llist = LinkedList(Node('Node1'))
llist.head.next = Node('Node2')
print(llist.head)

for node in llist:
    print(node)

