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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

    def remove(self, index):
        if index > self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                                                                Exercise
"""
# DLL: Swap First and Last (⚡ Interview Question)
# Swap the values of the first and last node
# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.
def swap_first_last(self):
    if self.length == 0:
        return None
    if self.length == 1:
        return self.head
    self.head.value, self.tail.value = self.tail.value, self.head.value
    return True

# DLL: Reverse (⚡ Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list.

def reverse(self):
    temp = self.head
    while temp:
         # swap the prev and next pointers of node points to
        temp.prev, temp.next = temp.next, temp.prev
        temp = temp.prev
    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head

# DLL: Palindrome Checker (⚡ Interview Question)
# Write a method to determine whether a given doubly linked list reads the same forwards and backwards.
def is_palindrome(self):
    if self.length <= 1:
        return True

    left = self.head
    right = self.tail
    """
    The method initializes two pointers, left and right, that point
    to the head and tail of the list, respectively. The method then iterates over
    half of the list, comparing the values of the nodes at each end of the list to
    see if they are the same.
    """
    for i in range(self.length//2):
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev
    return True

# DLL: Swap Nodes in Pairs (⚡ Interview Question)
# Example: 1-->2-->3-->4--> should become 2-->1-->4-->3-->
# Define a method to swap adjacent nodes in the doubly linked list.

def swap_pairs(self):
    # Initialize a dummy node and set its next node to the head of the list.
    dummy = Node(0)
    dummy.next = self.head
    # Set the prev variable to the dummy node.
    prev = dummy
    
    # Loop through the list while there are at least two more nodes to swap.
    while self.head and self.head.next:
        # Set first_node to the current head and second_node to the next node.
        first_node = self.head
        second_node = self.head.next
        
        # Modify the links to swap the nodes.
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        
        # Move the head of the list to the next pair of nodes to be swapped.
        self.head = first_node.next
        prev = first_node
        
    # Return the head of the list after swapping the nodes.
    self.head = dummy.next
