from tkinter import *
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            raise IndexError("delete from empty list")
        deleted_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            raise IndexError("delete from empty list")
        deleted_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node.data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class DLLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List Data Structure")
        self.root.state("zoomed")
        self.root.configure(bg='light blue')

        # Create GUI elements
        self.label = Label(root, text="Doubly Linked List Data Structure", font=("Arial", 20), bg="light blue")
        self.label.grid(row=0, column=0, columnspan=6, pady=10)

        self.entry_label = Label(self.root, text="Enter element:", font=("Arial", 14), bg="light blue")
        self.entry_label.grid(row=1, column=0, padx=10, pady=10)

        self.entry = Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        self.insert_beginning_button = Button(self.root, text="Insert at Beginning", font=("Arial", 14), command=self.insert_at_beginning)
        self.insert_beginning_button.grid(row=1, column=2, padx=10, pady=10)

        self.insert_end_button = Button(self.root, text="Insert at End", font=("Arial", 14), command=self.insert_at_end)
        self.insert_end_button.grid(row=1, column=3, padx=10, pady=10)

        self.delete_beginning_button = Button(self.root, text="Delete at Beginning", font=("Arial", 14), command=self.delete_at_beginning)
        self.delete_beginning_button.grid(row=2, column=2, padx=10, pady=10)

        self.delete_end_button = Button(self.root, text="Delete at End", font=("Arial", 14), command=self.delete_at_end)
        self.delete_end_button.grid(row=2, column=3, padx=10, pady=10)

        self.traverse_button = Button(self.root, text="Traverse", font=("Arial", 14), command=self.traverse_list)
        self.traverse_button.grid(row=2, column=4, padx=10, pady=10)

        self.status_label = Label(self.root, text="", font=("Arial", 14), bg="light blue")
        self.status_label.grid(row=3, column=0, columnspan=6, pady=10)

        # Add a frame to display the list with a scrollbar
        self.list_frame = Frame(self.root, bg="white")
        self.list_frame.grid(row=4, column=0, columnspan=6, pady=10, sticky="nsew")

        self.canvas = Canvas(self.list_frame, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.list_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=BOTTOM, fill=X)

        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.dll = DoublyLinkedList()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def insert_at_beginning(self):
        data = self.entry.get().strip()
        if data:
            self.dll.insert_at_beginning(data)
            self.entry.delete(0, END)
            self.update_status(f"Inserted at beginning: {data}")
            self.draw_list()
        else:
            messagebox.showwarning("Warning", "Element cannot be empty")

    def insert_at_end(self):
        data = self.entry.get().strip()
        if data:
            self.dll.insert_at_end(data)
            self.entry.delete(0, END)
            self.update_status(f"Inserted at end: {data}")
            self.draw_list()
        else:
            messagebox.showwarning("Warning", "Element cannot be empty")

    def delete_at_beginning(self):
        try:
            data = self.dll.delete_at_beginning()
            self.update_status(f"Deleted at beginning: {data}")
            self.draw_list()
        except IndexError:
            messagebox.showwarning("Warning", "List is empty")

    def delete_at_end(self):
        try:
            data = self.dll.delete_at_end()
            self.update_status(f"Deleted at end: {data}")
            self.draw_list()
        except IndexError:
            messagebox.showwarning("Warning", "List is empty")

    def traverse_list(self):
        elements = self.dll.traverse()
        self.update_status(f"Traversing the list: {' <--> '.join(elements)}")
        self.draw_list()

    def update_status(self, message):
        self.status_label.config(text=message)

    def draw_list(self):
        self.canvas.delete("all")
        if self.dll.head:
            x_start = 50
            y_start = 50
            box_width = 50
            box_height = 30
            padding = 10
            current = self.dll.head
            while current:
                x = x_start
                self.canvas.create_rectangle(x, y_start, x + box_width, y_start + box_height, fill="lightblue")
                self.canvas.create_text(x + box_width / 2, y_start + box_height / 2, text=current.data, font=("Arial", 12))
                x_start += box_width + padding
                current = current.next
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

if __name__ == "__main__":
    root = Tk()
    app = DLLApp(root)
    root.mainloop()
