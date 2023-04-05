class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node = self.root
        que = []
        res = []
        que.append(current_node)

        while len(que) > 0:
            current_node =  que.pop(0)
            res.append(current_node.value)
            if current_node.left is not None:
                que.append(current_node.left)
            if current_node.right is not None:
                que.append(current_node.right)
        return res
    
    def dfs_pre_order(self):
        res = []
        def traverse(current_node):
            res.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return res
    
    def dfs_post_order(self):
        res = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            res.append(current_node.value)
        traverse(self.root)
        return res
    def dfs_in_order(self):
        res = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            res.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
            
        traverse(self.root)
        return res
    
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())


# BST: Validate BST (⚡ Interview Question)
# You are tasked with writing a method called is_valid_bst in the 
# BinarySearchTree class that checks whether a binary search tree is a valid binary search tree.
def is_valid_bst(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)
    traverse(self.root)
    for i in range(1, len(node_values)):
        if node_values[i] <= node_values[i-1]:
            return False
    return True


