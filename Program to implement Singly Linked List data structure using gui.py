import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.update_listbox()
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.update_listbox()
    
    def delete_at_beginning(self):
        if self.is_empty():
            messagebox.showinfo("Empty List", "Linked List is empty")
            return None
        deleted_node = self.head
        self.head = self.head.next
        self.update_listbox()
        return deleted_node.data
    
    def delete_at_end(self):
        if self.is_empty():
            messagebox.showinfo("Empty List", "Linked List is empty")
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            self.update_listbox()
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        self.update_listbox()
        return deleted_node.data
    
    def traverse(self):
        current = self.head
        traverse_str = ""
        while current:
            traverse_str += str(current.data) + " -> "
            current = current.next
        traverse_str += "None"
        return traverse_str
    
    def update_listbox(self):
        traverse_str = self.traverse()
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, traverse_str)

class LinkedListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Singly Linked List Operations")
        self.configure(background='light blue')  # Set background color

        self.linked_list = SingleLinkedList()

        label = tk.Label(self, text="Singly Linked List Operations", padx=10, pady=10, font=("Arial", 16), bg='light blue')
        label.pack()

        self.entry_data = tk.Entry(self, width=30, font=("Arial", 14))
        self.entry_data.pack(pady=5)

        frame_buttons = tk.Frame(self, bg='light blue')
        frame_buttons.pack(pady=10)

        btn_insert_beginning = tk.Button(frame_buttons, text="Insert at Beginning", command=self.insert_beginning, font=("Arial", 14))
        btn_insert_beginning.grid(row=0, column=0, padx=5)

        btn_insert_end = tk.Button(frame_buttons, text="Insert at End", command=self.insert_end, font=("Arial", 14))
        btn_insert_end.grid(row=0, column=1, padx=5)

        btn_delete_beginning = tk.Button(frame_buttons, text="Delete at Beginning", command=self.delete_beginning, font=("Arial", 14))
        btn_delete_beginning.grid(row=0, column=2, padx=5)

        btn_delete_end = tk.Button(frame_buttons, text="Delete at End", command=self.delete_end, font=("Arial", 14))
        btn_delete_end.grid(row=0, column=3, padx=5)

        btn_traverse = tk.Button(frame_buttons, text="Traverse", command=self.traverse, font=("Arial", 14))
        btn_traverse.grid(row=0, column=4, padx=5)

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        global listbox
        listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set, width=50, font=("Arial", 14))
        listbox.pack(pady=10)
        self.scrollbar.config(command=listbox.yview)

    def insert_beginning(self):
        data = self.entry_data.get()
        if data:
            self.linked_list.insert_at_beginning(data)
            self.clear_entry()
        else:
            messagebox.showwarning("Empty Field", "Please enter data.")

    def insert_end(self):
        data = self.entry_data.get()
        if data:
            self.linked_list.insert_at_end(data)
            self.clear_entry()
        else:
            messagebox.showwarning("Empty Field", "Please enter data.")

    def delete_beginning(self):
        deleted_data = self.linked_list.delete_at_beginning()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", f"{deleted_data} is deleted from the beginning")

    def delete_end(self):
        deleted_data = self.linked_list.delete_at_end()
        if deleted_data is not None:
            messagebox.showinfo("Deleted", f"{deleted_data} is deleted from the end")

    def traverse(self):
        traverse_str = self.linked_list.traverse()
        messagebox.showinfo("Traversal", traverse_str)

    def clear_entry(self):
        self.entry_data.delete(0, tk.END)

if __name__ == "__main__":
    app = LinkedListApp()
    app.mainloop()
