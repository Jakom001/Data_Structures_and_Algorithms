class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    #  traverse the linked list
    def traverse(self):
        current = self.head
        print("None", end = " <-> ")
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.next
        print("None")
 
    # reverse traverse the linked list
    def reverse_traverse(self):
        current = self.tail
        print("None", end = " <-> ")
        while current is not None:
            print(f"{current.data} <-> ", end="") 
            current = current.prev
        print("None")
    # node count
    def node_count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
 
    # check if empty
    def is_empty(self):
        return self.head == None
 
    # append to empty list
    def append_to_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
 
    # insert at the end(append)
    def append(self, data):
        if self.is_empty():
            self.append_to_empty(data)
            return
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    # insert at beginning
    def insert_at_beginning(self, data):
        if self.is_empty():
            self.append_to_empty()
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    # insert at position
    def insert_at_position(self, position, data):
        if position < 0 or position > self.node_count():
            print("Invalid position")
            return
        elif position == 0:
            self.insert_at_beginning(data)
            return
        elif position == self.node_count():
            self.append(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            for i in range(position - 1):
                current = current.next
            next_node = current.next
            current.next = new_node
            next_node.prev = new_node
            new_node.prev = current
            new_node.next = next_node
 
    # delete from beginning
    def delete_from_beginning(self):
        if self.is_empty():
            print('Cannot delete from Empty')
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else: 
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            del current
    
    # delete from end
    def delete_from_end(self):
        if self.is_empty():
            print('Cannot delete from Empty')
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else: 
            current = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del current
 
    # delete from given position 
    def delete_from_position(self, position):
        if self.is_empty():
            print('Cannot delete from Empty')  
        elif position <= 0 or position > self.node_count():
            print('Invalid position')
        elif position == 1:
            self.delete_from_beginning()
        elif position == self.node_count():
            self.delete_from_end()
        else:
            current = self.head
            prev_node = next_node = None
            for i in range(position-1):
                current = current.next
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node
            del current
    # reverse
    def reverse(self):

        # no need to reverse in case of 0 or 1 nodes
        if self.node_count() < 2:
            return

        # start from head
        current = self.head
        while True:
            # swap previous and next node pointers
            current.prev, current.next = current.next, current.prev

            # move to the new previous node
            current = current.prev

            # repeat until you reach None
            if current == None:
                break

        # swap head and tail
        self.head, self.tail = self.tail, self.head
 
linked_list = DoublyLinkedList()
linked_list.append_to_empty(2)
linked_list.append(4)
linked_list.insert_at_beginning(1)
linked_list.insert_at_position(2, 3)
linked_list.traverse()
 
linked_list.delete_from_position(2)
linked_list.delete_from_beginning()
linked_list.delete_from_end()
linked_list.traverse()
