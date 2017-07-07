class Node:
    def __init__(self, value):
        self.value = value
        self.children = None

class Tree:
    def __init__(self, root=None):
        self.root = root

    def generate_test_tree(self):
        A = Node('A')
        B = Node('B')
        C = Node('C')
        D = Node('D')
        E = Node('E')
        F = Node('F')
        B.children = [A,C]
        E.children = [F]
        D.children = [B,E]
        tree.root = D
        
    def breath_first_traversal(self, node):
        if node.children == None:
            print(node.value)
            return
        else:
            print(node.value)
            
        
        pass
    
    def depth_first_preorder(self, node):
        if node.children == None:
            print(node.value)
            return
        else:
            print(node.value)
            for child in node.children:
                self.depth_first_preorder(child)

    def depth_first_postorder(self, node):
        if node.children == None:
            print(node.value)
            return
        else:
            for child in node.children:
                self.depth_first_postorder(child)
            print(node.value)


tree = Tree()
tree.generate_test_tree()
print("--BREATH FIRST TRAVERSAL--");
tree.breath_first_traversal(tree.root)
print("--DEPTH FIRST PREORDER--");
tree.depth_first_preorder(tree.root)
print("--DEPTH FIRST INORDER--");
#In order requires distinction between left and right
print("--DEPTH FIRST POSTORDER--");
tree.depth_first_postorder(tree.root)
