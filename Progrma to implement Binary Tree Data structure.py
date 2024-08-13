class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_larger_node = self._get_min(root.right)
            root.val = min_larger_node.val
            root.right = self._delete(root.right, min_larger_node.val)
        return root

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        res = []
        if root:
            res = self._inorder_traversal(root.left)
            res.append(root.val)
            res = res + self._inorder_traversal(root.right)
        return res

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self._preorder_traversal(root.left)
            res = res + self._preorder_traversal(root.right)
        return res

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, root):
        res = []
        if root:
            res = self._postorder_traversal(root.left)
            res = res + self._postorder_traversal(root.right)
            res.append(root.val)
        return res

def operation():
    bt = BinaryTree()
    while True:
        print("\nBinary Tree operation: \n1. Insert \n2. Delete \n3. Inorder Traverse \n4. Preorder Traverse \n5. Postorder Traverse \n6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            key = input("Enter the value: ")
            bt.insert(key)
            print(key,"inserted")
        elif choice == 2:
            key = input("Enter the value: ")
            bt.delete(key)
            print(key,"deleted")
        elif choice == 3:
            print("Inorder traversal: ", bt.inorder_traversal())
        elif choice == 4:
            print("Preorder traversal: ", bt.preorder_traversal())
        elif choice == 5:
            print("Postorder traversal: ", bt.postorder_traversal())
        elif choice == 6:
            print("Exiting")
            break
        else:
            print("Enter a vaild choice(1-6)")
            
operation()
        
