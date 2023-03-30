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
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        before =  None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

"""
Exercise
"""
# LL: Find Middle Node (⚡ Interview Question)
# Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute
def find_middle_node(self):
    """
    Traverse linked list using two-pointers. 
    Move one pointer by one and the other pointers by two. 
    When the fast pointer reaches the end, 
    the slow pointer will reach the middle of the linked list.
    """
    slow_runner = self.head
    fast_runner = self.head
    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner =fast_runner.next.next
    return slow_runner

# LL: Has Loop (⚡ Interview Question)
# Write a method to determine if the Linked List contains a loop.
def has_loop(self):
    """
    Traverse linked list using two pointers.
    Move one pointer(slow_p) by one and another pointer(fast_p) by two.
    If these pointers meet at the same node then there is a loop. 
    If pointers do not meet then the linked list doesn’t have a loop.
    """
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
def has_loop(self):
    """
    The idea is to insert the nodes in the hashmap and whenever 
    a node is encountered that is already present in the hashmap then return true.
    """
    s = set()
    temp = self.head
    while temp:
        if temp in s:
            return True
        s.add(temp)
        temp = temp.next
    return false

# LL: Remove Duplicates (⚡Interview Question)
# Remove all duplicates from the Linked List.
# https://www.prepbytes.com/blog/linked-list/remove-duplicates-from-an-unsorted-linked-list/
def remove_duplicates(self):
        values = set()
        prev = None
        curr = self.head
        while curr:
            if curr.value in values:
                prev.next = curr.next
                self.length -= 1
            else:
                values.add(curr.value)
                prev = curr
            curr = curr.next

# LL: Find Kth Node From End (⚡Interview Question)
# Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.
def find_kth_from_end(ll, k):
    # Initialize both slow and fast pointers to 
    # the head node of the linked list
    slow = fast = ll.head   
    
    # Move the fast pointer k nodes ahead of the slow pointer
    # If fast pointer reaches the end (None) before k nodes, 
    # the linked list is too short and kth node doesn't exist
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    # Move both pointers one node at a time until the fast 
    # pointer reaches the end of the linked list (None).
    # The slow pointer will now be pointing at the kth node 
    # from the end of the linked list.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # Return the kth node from the end of the linked list
    return slow
def find_kth_from_end(LL, k):    
    """
    Calculate the length of the Linked List. Let the length be len. 
    Print the (len – n + 1)th node from the beginning of the Linked List. 
    """
    temp = LL.head
    count = 0
    while temp:
        temp = temp.next
        count += 1
    if k > count:
        return None
        
    result = LL.head
    for i in range(0, count-k):
        result = result.next
    return result

# LL: Reverse Between (⚡Interview Question)
# You are given a singly linked list and two integers m and n. 
# Your task is to write a method reverse_between within the LinkedList class 
# that reverses the nodes of the linked list 
# from index m to index n (inclusive) in one pass and in-place

def reverse_between(self, m, n):
    # If the linked list is empty, then return None.
    if self.head == None:
        return None
    
    # Create a dummy node and connect it to the head.
    dummy = Node(0)
    dummy.next = self.head
    prev = dummy
    
    # Move prev to the node at position m.
    for i in range(m):
        prev = prev.next
        
    # set current to the next node of prev.
    current = prev.next
    
    # Reverse the linked list from position m to n.
    for i in range(n-m):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp
        
    # update the head of the linked list with the next node of the dummy.
    self.head = dummy.next
