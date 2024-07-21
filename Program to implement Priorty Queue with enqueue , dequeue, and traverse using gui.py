from tkinter import *
from tkinter import messagebox, simpledialog

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.size

    def set_size(self, size):
        self.size = size

    def enqueue(self, process, priority):
        if self.is_full():
            raise OverflowError("Priority Queue is full")
        else:
            self.queue.append((process, priority))
            self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[0]
        else:
            raise IndexError("dequeue from empty priority queue")

    def traverse(self):
        if self.is_empty():
            return []
        else:
            return self.queue

class PriorityQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Priority Queue Data Structure")
        self.root.configure(bg='light blue')

        # Create GUI elements
        self.label = Label(root, text="Priority Queue Data Structure", font=("Arial", 20), bg="light blue")
        self.label.grid(row=0, column=0, columnspan=6, pady=10)

        self.label = Label(root, text="Name:Jyoti Kumbhar", font=("Arial", 20), bg="light blue")
        self.label.grid(row=1, column=0, columnspan=6, pady=10)

        self.label = Label(root, text="Roll No.S089", font=("Arial", 20), bg="light blue")
        self.label.grid(row=1, column=1, columnspan=6, pady=10)

        self.size_label = Label(self.root, text="Enter size of queue:", font=("Arial", 14), bg="light blue")
        self.size_label.grid(row=2, column=0, padx=10, pady=10)

        self.size_entry = Entry(self.root, width=20, font=("Arial", 14))
        self.size_entry.grid(row=2, column=1, padx=10, pady=10)

        self.set_size_button = Button(self.root, text="Set Size", font=("Arial", 14), command=self.set_queue_size)
        self.set_size_button.grid(row=2, column=2, padx=10, pady=10)

        self.entry_label = Label(self.root, text="Enter process:", font=("Arial", 14), bg="light blue")
        self.entry_label.grid(row=3, column=0, padx=10, pady=10)

        self.priority_label = Label(self.root, text="Enter priority:", font=("Arial", 14), bg="light blue")
        self.priority_label.grid(row=3, column=2, padx=10, pady=10)

        self.entry = Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=3, column=1, padx=10, pady=10)

        self.priority_entry = Entry(self.root, width=20, font=("Arial", 14))
        self.priority_entry.grid(row=3, column=3, padx=10, pady=10)

        self.enqueue_button = Button(self.root, text="Enqueue", font=("Arial", 14), command=self.enqueue_element)
        self.enqueue_button.grid(row=3, column=4, padx=10, pady=10)

        self.dequeue_button = Button(self.root, text="Dequeue", font=("Arial", 14), command=self.dequeue_element)
        self.dequeue_button.grid(row=3, column=5, padx=10, pady=10)

        self.traverse_button = Button(self.root, text="Traverse", font=("Arial", 14), command=self.traverse_queue)
        self.traverse_button.grid(row=4, column=0, columnspan=6, padx=10, pady=10)

        self.status_label = Label(self.root, text="", font=("Arial", 14), bg="light blue")
        self.status_label.grid(row=5, column=0, columnspan=6, pady=10)

        self.queue_display_label = Label(self.root, text="", font=("Arial", 14), bg="light blue")
        self.queue_display_label.grid(row=6, column=0, columnspan=6, pady=10)

        self.queue = PriorityQueue()

    def set_queue_size(self):
        try:
            size = int(self.size_entry.get().strip())
            if size <= 0:
                messagebox.showerror("Error", "Queue size must be greater than zero")
            else:
                self.queue.set_size(size)
                messagebox.showinfo("Info", f"Queue size set to {size}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the size")

    def enqueue_element(self):
        try:
            process = self.entry.get().strip()
            priority = int(self.priority_entry.get().strip())
            if process:
                self.queue.enqueue(process, priority)
                self.entry.delete(0, END)
                self.priority_entry.delete(0, END)
                self.update_status(f"Enqueued: {process} with priority {priority}")
                self.draw_queue()
            else:
                messagebox.showwarning("Warning", "Process cannot be empty")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid priority")
        except OverflowError:
            messagebox.showerror("Error", "Priority Queue is full")

    def dequeue_element(self):
        try:
            process = self.queue.dequeue()
            self.update_status(f"Dequeued: {process}")
            self.draw_queue()
        except IndexError:
            messagebox.showwarning("Warning", "Priority Queue is empty")

    def traverse_queue(self):
        elements = self.queue.traverse()
        if elements:
            self.update_status(f"Queue elements: {' -> '.join(f'{process}({priority})' for process, priority in elements)}")
        else:
            self.update_status("Priority Queue is empty")
        self.draw_queue()

    def update_status(self, message):
        self.status_label.config(text=message)

    def draw_queue(self):
        elements = self.queue.traverse()
        if elements:
            queue_str = " -> ".join(f"{process}({priority})" for process, priority in elements)
            self.queue_display_label.config(text=f"Queue: {queue_str}")
        else:
            self.queue_display_label.config(text="Queue: ")

if __name__ == "__main__":
    root = Tk()
    app = PriorityQueueApp(root)
    root.mainloop()
