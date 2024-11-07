import tkinter as tk
from tkinter import messagebox

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solver")
        self.root.state('zoomed')
        self.root.configure(bg='lightblue')

        # Configure grid layout
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        tk.Label(root, text="Jyoti Kumbhar S089",font=('arial',14), bg='lightblue').grid(row=0, column=1, sticky='w')
        tk.Label(root, text="Hash Table",font=('arial',14), bg='lightblue').grid(row=0, column=2, sticky='w')

        tk.Label(root, text="Size of array:",font=('arial',14), bg='lightblue').grid(row=1, column=1, sticky='w')
        self.entry_size = tk.Entry(root, font=('arial',14))
        self.entry_size.grid(row=1, column=2)

        tk.Label(root, text="Key:",font=('arial',14), bg='lightblue').grid(row=2, column=1, sticky='w')
        self.entry_key = tk.Entry(root, font=('arial',14))
        self.entry_key.grid(row=2, column=2)

        tk.Label(root, text="Value:",font=('arial',14), bg='lightblue').grid(row=2, column=3, sticky='w')
        self.entry_value = tk.Entry(root, font=('arial',14))
        self.entry_value.grid(row=2, column=4)

        self.button1 = tk.Button(root, text="Insert", command=self.insert, font=('arial',14), bg='lightblue')
        self.button1.grid(row=3, column=1)

        self.button2 = tk.Button(root, text="Delete", command=self.delete, font=('arial',14), bg='lightblue')
        self.button2.grid(row=3, column=2)

        self.button3 = tk.Button(root, text="Search", command=self.search, font=('arial',14), bg='lightblue')
        self.button3.grid(row=3, column=3)

        self.button4 = tk.Button(root, text="Traverse", command=self.traverse, font=('arial',14), bg='lightblue')
        self.button4.grid(row=3, column=4)

        self.result_label = tk.Label(root, text="",font=('arial',14), bg='lightblue')
        self.result_label.grid(row=4, column=1, columnspan=4, sticky='w')
        
    def size(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given key."""
        return key % self.size

    def insert(self):
        """Insert a key-value pair into the hash table."""
        try:
            key = int(self.entry_key.get())
            value = self.entry_value.get()
            size = int(self.entry_size.get())
            if not hasattr(self, 'table'):
                self.size(size)
            index = self.hash_function(key)
            self.table[index] = (key, value)
            self.result_label.config(text= f"Inserted key {key} with value {value}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter integers for key and size.")

    def delete(self):
        """Delete the value associated with the given key."""
        try:
            key = int(self.entry_key.get())
            index = self.hash_function(key)
            if self.table[index] and self.table[index][0] == key:
                self.table[index] = None
                self.result_label.config(text= f"Deleted key {key}")
            else:
                messagebox.showerror("Error", f"Key {key} not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter an integer for key.")

    def search(self):
        """Search for the value associated with the given key."""
        try:
            key = int(self.entry_key.get())
            index = self.hash_function(key)
            if self.table[index] and self.table[index][0] == key:
                value = self.table[index][1]
                self.result_label.config(text= f"Key {key} has value {value}")
            else:
                messagebox.showerror("Error", f"Key {key} not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter an integer for key.")

    def traverse(self):
        """Traverse and print all key-value pairs in the hash table."""
        result = []
        for index, item in enumerate(self.table):
            if item is not None:
                key, value = item
                result.append(f"Index {index}: Key {key}, Value {value} \n")
        if result:
            self.result_label.config(text= "".join(result))
        else:
            messagebox.showinfo("Hash Table", "Hash table is empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = gui(root)
    root.mainloop()
