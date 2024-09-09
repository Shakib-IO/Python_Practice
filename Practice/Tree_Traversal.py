from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfsTraversal(self, root: TreeNode) -> list:
        results = []
        queue = deque()
        queue.append(root)
        while queue:
            current_node = queue.popleft()
            results.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results

    def dfsPreOrder(self, root: TreeNode) -> list:
        stack = []
        results = []

        stack.append(root)
        while stack:
            current_node = stack.pop()
            results.append(current_node.val)

            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)
        return results
    
    def dfsInOrder(self, root: TreeNode) -> list:
        stack = []
        results = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            results.append(current.val)
            current = current.right

        return results
    
    def dfsPostOrder(self, root: TreeNode) -> list:
        if root is None:
            return []
        
        result = []
        stack = []
        last_visited = None
        
        current = root
        
        while stack or current:
            # Go to the leftmost node
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                # If right node exists and traversal is from left node, then move right
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.val)
                    last_visited = stack.pop()
                    current = None
        
        return result
            

# Example usage:
# Constructing a binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Creating a Solution object and calling bfsTraversal
sol = Solution()
print(sol.bfsTraversal(root))  # Output: [1, 2, 3, 4, 5, 6]
print(sol.dfsPreOrder(root))  # Output: [1, 2, 4, 5, 3, 6]
print(sol.dfsInOrder(root)) # Output: [4, 2, 5, 1, 3, 6]
print(sol.dfsPostOrder(root)) # Output: [4, 5, 2, 6, 3, 1]
