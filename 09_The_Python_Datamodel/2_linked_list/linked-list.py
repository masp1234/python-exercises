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

    def __repr__(self):
        return f'{self.__dict__}'

    def __iter__(self):
        self._current_node = self.head
        return self
    
    def __next__(self):
        if self._current_node == None:
            raise StopIteration
        else:
            current_element = self._current_node
            self._current_node = self._current_node.next
            return current_element
    def __len__(self):
        length = 0
        for node in self:
            length += 1
        return length
    
    def __add__(self, other):
        # Should return a new list instead of mutating "self"
        last_node = self[len(self) - 1]
        last_node.next = other.head

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError(f'the index: {index} is out of range')
        counter = 0
        for node in self:
            if index == counter:
                return node
            counter += 1
            


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
llist.head.next.next = Node('Node3')


element = llist[0]
print(element)

element = llist[1]
print(element)

element = llist[2]
print(element)
print(len(llist))

newllist = LinkedList(Node('Hello first node in second list'))
newllist.head.next = Node('second element in second list')
llist + newllist
print(len(llist))
print(llist)
