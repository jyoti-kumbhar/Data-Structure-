from tkinter import *
from tkinter import messagebox

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

class BinaryTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Tree Operations")
        self.root.state("zoomed")
        self.root.configure(bg="light blue")

        # Title
        self.title_label = Label(root, text="Binary Tree Operations", font=("Arial", 20), bg="light blue")
        self.title_label.grid(row=0, column=0, columnspan=6, pady=10)

        # Name and Roll No
        self.name_label = Label(root, text="Name: Jyoti Kumbhar", font=("Arial", 14), bg="light blue")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.rollno_label = Label(root, text="Roll No: S089", font=("Arial", 14), bg="light blue")
        self.rollno_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Input and Buttons
        self.entry_label = Label(self.root, text="Enter element:", font=("Arial", 14), bg="light blue")
        self.entry_label.grid(row=2, column=0, padx=10, pady=10)

        self.entry = Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=2, column=1, padx=10, pady=10)

        self.insert_button = Button(self.root, text="Insert", font=("Arial", 14), command=self.insert_value)
        self.insert_button.grid(row=2, column=2, padx=10, pady=10)

        self.delete_button = Button(self.root, text="Delete", font=("Arial", 14), command=self.delete_value)
        self.delete_button.grid(row=2, column=3, padx=10, pady=10)

        self.inorder_button = Button(self.root, text="Inorder Traversal", font=("Arial", 14), command=self.show_inorder)
        self.inorder_button.grid(row=3, column=2, padx=10, pady=10)

        self.preorder_button = Button(self.root, text="Preorder Traversal", font=("Arial", 14), command=self.show_preorder)
        self.preorder_button.grid(row=3, column=3, padx=10, pady=10)

        self.postorder_button = Button(self.root, text="Postorder Traversal", font=("Arial", 14), command=self.show_postorder)
        self.postorder_button.grid(row=3, column=4, padx=10, pady=10)

        self.status_label = Label(self.root, text="", font=("Arial", 14), bg="light blue")
        self.status_label.grid(row=4, column=0, columnspan=6, pady=10)

        # Tree display with scrollbar
        self.tree_frame = Frame(self.root, bg="white")
        self.tree_frame.grid(row=5, column=0, columnspan=6, pady=10, sticky="nsew")

        self.canvas = Canvas(self.tree_frame, bg="white", height=450)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.tree_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.update_scrollregion)

        self.bt = BinaryTree()

    def update_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def insert_value(self):
        key = self.entry.get().strip()
        if key:
            self.bt.insert(int(key))
            self.entry.delete(0, END)
            self.update_status(f"Inserted: {key}")
            self.draw_tree()
        else:
            messagebox.showwarning("Warning", "Element cannot be empty")

    def delete_value(self):
        key = self.entry.get().strip()
        if key:
            self.bt.delete(int(key))
            self.entry.delete(0, END)
            self.update_status(f"Deleted: {key}")
            self.draw_tree()
        else:
            messagebox.showwarning("Warning", "Element cannot be empty")

    def show_inorder(self):
        traversal = self.bt.inorder_traversal()
        self.update_status(f"Inorder Traversal: {traversal}")

    def show_preorder(self):
        traversal = self.bt.preorder_traversal()
        self.update_status(f"Preorder Traversal: {traversal}")

    def show_postorder(self):
        traversal = self.bt.postorder_traversal()
        self.update_status(f"Postorder Traversal: {traversal}")

    def update_status(self, message):
        self.status_label.config(text=message)

    def draw_tree(self):
        self.canvas.delete("all")
        if self.bt.root:
            self._draw_node(self.bt.root, self.canvas.winfo_width() // 2, 50, self.canvas.winfo_width() // 6)

    def _draw_node(self, node, x, y, x_offset):
        if node:
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.val), font=("Arial", 14))
            if node.left:
                self.canvas.create_line(x, y + 20, x - x_offset, y + 50)
                self._draw_node(node.left, x - x_offset, y + 70, x_offset // 2)
            if node.right:
                self.canvas.create_line(x, y + 20, x + x_offset, y + 50)
                self._draw_node(node.right, x + x_offset, y + 70, x_offset // 2)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

if __name__ == "__main__":
    root = Tk()
    app = BinaryTreeApp(root)
    root.mainloop()
