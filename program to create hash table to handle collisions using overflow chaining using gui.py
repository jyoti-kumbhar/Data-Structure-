import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solver")
        self.root.state('zoomed')
        self.root.configure(bg='lightblue')

        # Configure grid layout
        self.root.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.hash_table = None

        tk.Label(root, text="Jyoti Kumbhar S089", font=('arial', 14), bg='lightblue').grid(row=0, column=1, sticky='w')
        tk.Label(root, text="Hash Table", font=('arial', 14), bg='lightblue').grid(row=0, column=2, sticky='w')

        tk.Label(root, text="Size of array:", font=('arial', 14), bg='lightblue').grid(row=1, column=1, sticky='w')
        self.entry_size = tk.Entry(root, font=('arial', 14))
        self.entry_size.grid(row=1, column=2)

        tk.Label(root, text="Key:", font=('arial', 14), bg='lightblue').grid(row=2, column=1, sticky='w')
        self.entry_key = tk.Entry(root, font=('arial', 14))
        self.entry_key.grid(row=2, column=2)

        tk.Label(root, text="Value:", font=('arial', 14), bg='lightblue').grid(row=2, column=3, sticky='w')
        self.entry_value = tk.Entry(root, font=('arial', 14))
        self.entry_value.grid(row=2, column=4)

        self.button1 = tk.Button(root, text="Insert", command=self.insert, font=('arial', 14), bg='lightblue')
        self.button1.grid(row=3, column=1)

        self.button2 = tk.Button(root, text="Delete", command=self.delete, font=('arial', 14), bg='lightblue')
        self.button2.grid(row=3, column=2)

        self.button3 = tk.Button(root, text="Search", command=self.search, font=('arial', 14), bg='lightblue')
        self.button3.grid(row=3, column=3)

        self.button4 = tk.Button(root, text="Traverse", command=self.traverse, font=('arial', 14), bg='lightblue')
        self.button4.grid(row=3, column=4)

        self.result_label = tk.Label(root, text="", font=('arial', 14), bg='lightblue')
        self.result_label.grid(row=4, column=1, columnspan=4, sticky='w')

    def initialize_table(self):
        """Initializes the hash table if it's not already initialized."""
        if self.hash_table is None:
            try:
                size = int(self.entry_size.get())
                self.hash_table = HashTable(size)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer for the size.")

    def insert(self):
        self.initialize_table()
        if self.hash_table:
            try:
                key = int(self.entry_key.get())
                value = self.entry_value.get()
                self.hash_table.insert(key, value)
                self.result_label.config(text=f"Inserted: {key} -> {value}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter integers for key.")

    def delete(self):
        self.initialize_table()
        if self.hash_table:
            try:
                key = int(self.entry_key.get())
                self.hash_table.delete(key)
                self.result_label.config(text=f"Deleted key: {key}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter an integer for key.")

    def search(self):
        self.initialize_table()
        if self.hash_table:
            try:
                key = int(self.entry_key.get())
                result = self.hash_table.search(key)
                if result is not None:
                    self.result_label.config(text=f"Found: {key} -> {result}")
                else:
                    self.result_label.config(text=f"Key {key} not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter an integer for key.")

    def traverse(self):
        self.initialize_table()
        if self.hash_table:
            result = self.hash_table.traverse()
            self.result_label.config(text=result)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def traverse(self):
        result = []
        for index, node in enumerate(self.table):
            current = node
            while current:
                result.append(f"Index {index}: Key {current.key}, Value {current.value}")
                current = current.next
        return "\n".join(result) if result else "Hash table is empty."

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()