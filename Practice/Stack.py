# Stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        if self.height == 0:
            return None
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
s = Stack(11)
s.push(100)
s.push(90)
s.print_stack()
print("-------")
s.pop()
s.print_stack()

"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                                                                Exercise
"""
