#Program to implement Priority Queue using a list and the heapq module for efficient operations with gui
import heapq
import tkinter as tk
from tkinter import messagebox, simpledialog

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def set_size(self, size):
        self.size = int(size)

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item, priority):
        if len(self.queue) >= self.size:
            return "Overflow. Cannot Enqueue item"
        heapq.heappush(self.queue, (int(priority), item))
        return None

    def dequeue(self):
        if self.is_empty():
            return "Underflow. Cannot Dequeue"
        return heapq.heappop(self.queue)[1]
    
    def peek(self):
        if self.is_empty():
            return "Underflow. Cannot Peek"
        return heapq.nsmallest(1, self.queue)[0][1]
    
    def traverse(self):
        if self.is_empty():
            return "Underflow. Cannot Traverse."
        return "\n".join(f"Priority: {i} Item: {j}" for i, j in self.queue)

class PriorityQueueGUI:
    def __init__(self, root):
        self.pq = PriorityQueue()
        self.root = root
        self.root.title("Priority Queue GUI")
        self.root.configure(bg='light blue')
        self.root.state('zoomed')
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Priority Queue Operations", font=('Arial', 20), bg='light blue')
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Size Entry and Label
        self.size_label = tk.Label(self.root, text="Queue Size:", font=('Arial', 20), bg='light blue')
        self.size_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.size_entry = tk.Entry(self.root, font=('Arial', 20))
        self.size_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Enqueue Button
        self.enqueue_button = tk.Button(self.root, text="Enqueue", font=('Arial', 20), command=self.enqueue)
        self.enqueue_button.grid(row=2, column=0, padx=10, pady=5)

        # Dequeue Button
        self.dequeue_button = tk.Button(self.root, text="Dequeue", font=('Arial', 20), command=self.dequeue)
        self.dequeue_button.grid(row=2, column=1, padx=10, pady=5)

        # Peek Button
        self.peek_button = tk.Button(self.root, text="Peek", font=('Arial', 20), command=self.peek)
        self.peek_button.grid(row=2, column=2, padx=10, pady=5)

        # Traverse Button
        self.traverse_button = tk.Button(self.root, text="Traverse", font=('Arial', 20), command=self.traverse)
        self.traverse_button.grid(row=2, column=3, padx=10, pady=5)

        # Output Text
        self.output_text = tk.Text(self.root, height=15, width=80, font=('Arial', 16), wrap='word')
        self.output_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Configure column and row weights
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

    def enqueue(self):
        size = self.size_entry.get()
        if not self.pq.size:
            self.pq.set_size(size)
        item = self.get_input("Enter the item:")
        priority = self.get_input(f"Enter the priority of {item}:")
        result = self.pq.enqueue(item, priority)
        if result:
            self.show_message("Error", result)
        else:
            self.show_message("Success", f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        result = self.pq.dequeue()
        if result.startswith("Underflow"):
            self.show_message("Error", result)
        else:
            self.show_message("Success", f"Dequeued: {result}")

    def peek(self):
        result = self.pq.peek()
        if result.startswith("Underflow"):
            self.show_message("Error", result)
        else:
            self.show_message("Success", f"Peek: {result}")

    def traverse(self):
        result = self.pq.traverse()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.root)
    def show_message(self, title, message):
        messagebox.showinfo(title, message)
if __name__ == "__main__":
    root = tk.Tk()
    app = PriorityQueueGUI(root)
    root.mainloop()