"""
Binary Tree
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, node, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if node != None:
            if node.value == find_val:
                return True
            else:
                return self.preorder_search(node.left, find_val) or self.preorder_search(node.right, find_val)
        return False

    def preorder_print(self, node, traversal):
        if node != None:
            traversal += (str(node.value) + "-")
            traversal = self.preorder_print(node.left, traversal)
            traversal = self.preorder_print(node.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()

"""
Binary Search Tree
Assume that two nodes with the same value won't be inserted into the tree. 
"""

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_node(self.root, Node(new_val))

    def insert_node(self, node, new_node):
        if new_node.value < node.value:
            if node.left == None:
                node.left = new_node
            else:
                self.insert_node(node.left, new_node)
        elif new_node.value > node.value:
            if node.right == None:
                node.right = new_node
            else:
                self.insert_node(node.left, new_node)

    def search(self, find_val):
        return self.search_node(self.root, find_val)

    def search_node(self, node, find_val):
        if node.value == find_val:
            return True
        else:
            if find_val < node.value and node.left != None:
                return self.search_node(node.left, find_val)
            elif find_val > node.value and node.right != None:
                return self.search_node(node.right, find_val)
        return False
                        
    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, node, traversal):
        if node != None:
            traversal += (str(node.value) + "-")
            traversal = self.preorder_print(node.left, traversal)
            traversal = self.preorder_print(node.right, traversal)
        return traversal
    
# Set up tree
tree2 = BST(4)

# Insert elements
tree2.insert(2)
tree2.insert(1)
tree2.insert(3)
tree2.insert(5)
print tree2.print_tree()


# Check search
# Should be True
print tree2.search(4)
# Should be False
print tree2.search(6)
