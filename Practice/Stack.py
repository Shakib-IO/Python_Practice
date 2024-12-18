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
# Stack: Push for Stack That Uses List (⚡ Interview Question)
class Stack:
    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
            
    def push(self, value):
        self.stack_list.append(value)

# Stack: Pop for Stack That Uses List (⚡ Interview Question)
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

# Stack: Reverse String (⚡Interview Question)
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def reverse_string(ss:str):
    stack = Stack()
    reverse_string = ""
    for char in ss:
        stack.push(char)
    while not stack.is_empty():
        reverse_string += stack.pop()
    return reverse_string

# Stack: Parentheses Balanced (⚡ Interview Question)
def is_balanced_parentheses(parentheses:str):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()
 
balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'
print(is_balanced_parentheses(balanced_parentheses))

# Stack: Sort Stack (⚡ Interview Question)
def sort_stack(stack):
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()
 
    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()
 
        # While the additional stack is not empty and 
        #the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())
 
        # Add the current element to the additional stack
        additional_stack.push(temp)
 
    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())

