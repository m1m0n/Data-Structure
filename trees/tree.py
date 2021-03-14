class BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None        
    
    def insert(self, data):
        new_node = BinTreeNode(data)
            # Left
        if data < self.data :
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(data)

            # Right
        elif data > self.data:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(data)
        else:
            self.data = data
        

    def preorder(self, subtree): # root - left - right
        if subtree is not None:
            print(subtree.data, end=" ")
            self.preorder(subtree.left)
            self.preorder(subtree.right)

    
    def inorder(self, subtree): # left - root - right --> ascending 
        if subtree is not None:
            self.preorder(subtree.left)
            print(subtree.data, end=" ")
            self.preorder(subtree.right)

    def rev_inorder(self, subtree): # right - root - left --> descending
        if subtree is not None:
            self.rev_inorder(subtree.right)
            print(subtree.data, end=" ")
            self.rev_inorder(subtree.left)
    
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


    def max_depth(self, root): # max depth = height
        if root == None:
            return -1
        else:
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)
            return max(left, right) + 1
    
    def level_order(self, subtree):
        h = self.max_depth(subtree)
        for i in range(1, h+1):
            self.print_level(subtree, i)
    
    def print_level(self, subtree, level):
        if subtree is None:
            return
        if level == 1:
            print(subtree.data, end=" ")
        elif level > 1:
            self.print_level(subtree.left,level - 1 )
            self.print_level(subtree.right, level - 1)
    
def search(root, key):
    if key == root.data:
        return "Found!"

    if key < root.data:
        return search(root.left, key)
    elif key > root.data:
        return search(root.right, key)

    
def remove_leaves(root):
    if root == None :
        return None
    if root.left == None and root.right == None:
        return None

    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root
if __name__ == "__main__":
    root = BinTreeNode(12)
    root.insert(6)
    root.insert(2)
    root.insert(14)
    root.insert(3)
    root.insert(13)
    root.insert(11)
    root.insert(1)
    print(search(root, 443))
    # remove_leaves(root)
    # root.inorder(root)
    # print("PreOrder : ")
    # root.inorder(root)
    # root.level_order(root)
    # root.rev_inorder(root)

    # print(root.find_min())
    # print(root.find_max())
    # print(root.max_depth(root))