class BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        
    
    def insert(self, data):
        if data < self.data :
            if self.left is None:
                self.left = BinTreeNode(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinTreeNode(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
        

    def preorder(self, subtree): # root - left - right
        if subtree is not None:
            print(subtree.data, end=" ")
            self.preorder(subtree.left)
            self.preorder(subtree.right)

    
    def inorder(self, subtree): # left - root - right
        if subtree is not None:
            self.preorder(subtree.left)
            print(subtree.data, end=" ")
            self.preorder(subtree.right)
    
    def postorder(self, subtree): # left - right - root
        if subtree is not None:
            self.preorder(subtree.left)
            self.preorder(subtree.right)
            print(subtree.data, end=" ")
    
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()


    def max_depth(self, root):
        if not root:
            return -1
        else:
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)
            return max(left, right) + 1
    

    
if __name__ == "__main__":
    root = BinTreeNode(12)
    root.insert(6)
    root.insert(2)
    root.insert(14)
    root.insert(3)
    root.insert(13)
    root.insert(11)
    root.preorder(root)
