# Python Deque

# Completed implementation of a deque.py

class Deque:

    def __init__(self):
        self.item = []
    
    def is_empty(self, item):
        return self.item == []
    
    def add_front(self, item):
        self.item.append(item)
    
    def add_rear(self, item):
        self.item.insert(0, item)
    
    def remove_front(self):
        return self.item.pop()
    
    def remove_rear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

# Palindrome Checker

from Deque import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)
    
    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal

print(pal_checker("radar"))

