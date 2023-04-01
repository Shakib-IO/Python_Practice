# Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1
    
    def print_q(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):  #O(1) 
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1 

    def dequeue(self): # O(1)
        if self.height == 0:
            return None
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return temp

q = Queue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.print_q()
print("----")
q.dequeue()
q.print_q()



"""
Queue Using Stacks: Enqueue (⚡Interview Question)
You are given a class MyQueue which implements a queue using two stacks. 
Your task is to implement the enqueue method which should add an element to the back of the queue.
"""
  def enqueue(self, value):
  # Transfer all elements from stack1 to stack2
      while len(self.stack1) > 0:
          self.stack2.append(self.stack1.pop())

      # Add the new element to the bottom of stack1
      self.stack1.append(value)

      # Transfer all elements back from stack2 to stack1
      while len(self.stack2) > 0:
          self.stack1.append(self.stack2.pop())
