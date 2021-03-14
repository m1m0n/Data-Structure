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

    def build_tree(self, arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
            self.insert(arr[i])
        

    
if __name__ == "__main__":
    pre = [10, 5, 1, 7, 40, 50]
    print("[+] Build Tree from PreOrder Traversal ...")
    root = BinTreeNode(pre[0])
    root.build_tree(pre)

    print("\n[+] PreOrder Traversal")
    root.preorder(root)

    print("\n[+] InOrder Traversal")
    root.inorder(root)

    print("\n[+] PostOrder Traversal")
    root.postorder(root)
    