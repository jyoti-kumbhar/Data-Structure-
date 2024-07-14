from tkinter import *
from tkinter import messagebox

class Queue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def enqueue(self, element):
        if self.size() < self.max_size:
            self.elements.append(element)
        else:
            raise IndexError("enqueue into full queue")

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

class QueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Data Structure")
        self.root.state("zoomed")
        self.root.configure(bg='light blue')

        # Create GUI elements
        self.label = Label(root, text="Queue Data Structure", font=("Arial", 20), bg="light blue")
        self.label.grid(row=0, column=0, columnspan=6, pady=10)

        self.size_label = Label(root, text="Enter queue size:", font=("Arial", 14), bg="light blue")
        self.size_label.grid(row=1, column=0, padx=10, pady=10)

        self.size_entry = Entry(root, width=10, font=("Arial", 14))
        self.size_entry.grid(row=1, column=1, padx=10, pady=10)

        self.size_button = Button(root, text="Set Size", font=("Arial", 14), command=self.set_queue_size)
        self.size_button.grid(row=1, column=2, padx=10, pady=10)

        self.entry_label = Label(self.root, text="Enter element:", font=("Arial", 14), bg="light blue")
        self.entry_label.grid(row=4, column=0, padx=10, pady=10)

        self.entry = Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=4, column=1, padx=10, pady=10)

        self.enqueue_button = Button(self.root, text="Enqueue", font=("Arial", 14), command=self.enqueue_element)
        self.enqueue_button.grid(row=4, column=2, padx=10, pady=10)

        self.dequeue_button = Button(self.root, text="Dequeue", font=("Arial", 14), command=self.dequeue_element)
        self.dequeue_button.grid(row=4, column=3, padx=10, pady=10)

        self.peek_button = Button(self.root, text="Peek", font=("Arial", 14), command=self.peek_element)
        self.peek_button.grid(row=4, column=4, padx=10, pady=10)

        self.is_empty_button = Button(self.root, text="Is Empty", font=("Arial", 14), command=self.check_is_empty)
        self.is_empty_button.grid(row=4, column=5, padx=10, pady=10)

        self.status_label = Label(self.root, text="Size: 0", font=("Arial", 14), bg="light blue")
        self.status_label.grid(row=5, column=0, columnspan=6, pady=10)

        # Add a frame to display the queue with a scrollbar
        self.queue_frame = Frame(self.root, bg="white")
        self.queue_frame.grid(row=6, column=0, columnspan=6, pady=10, sticky="nsew")
        
        self.canvas = Canvas(self.queue_frame, width=600, height=200, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        self.scrollbar = Scrollbar(self.queue_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=BOTTOM, fill=X)
        
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.queue = None

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def set_queue_size(self):
        try:
            size = int(self.size_entry.get())
            if size > 0:
                self.queue = Queue(size)
                self.update_status(f"Queue size set to {size}")
                self.draw_queue()
            else:
                self.update_status("Size should be greater than zero")
        except ValueError:
            self.update_status("Invalid input. Enter a valid integer.")

    def enqueue_element(self):
        if self.queue:
            element = self.entry.get().strip()
            if element:
                try:
                    self.queue.enqueue(element)
                    self.entry.delete(0, END)
                    self.update_status(f"Enqueued: {element}")
                    self.draw_queue()
                except IndexError:
                    messagebox.showwarning("Warning", "Queue is full")
            else:
                messagebox.showwarning("Warning", "Element cannot be empty")
        else:
            messagebox.showerror("Error", "Set queue size first")

    def dequeue_element(self):
        if self.queue:
            try:
                element = self.queue.dequeue()
                self.update_status(f"Dequeued: {element}")
                self.draw_queue()
            except IndexError:
                messagebox.showwarning("Warning", "Queue is empty")
        else:
            messagebox.showerror("Error", "Set queue size first")

    def peek_element(self):
        if self.queue:
            try:
                element = self.queue.peek()
                messagebox.showinfo("Peek", f"Front element: {element}")
            except IndexError:
                messagebox.showwarning("Warning", "Queue is empty")
        else:
            messagebox.showerror("Error", "Set queue size first")

    def check_is_empty(self):
        if self.queue:
            if self.queue.is_empty():
                messagebox.showinfo("Is Empty", "Queue is empty")
            else:
                messagebox.showinfo("Is Empty", "Queue is not empty")
        else:
            messagebox.showerror("Error", "Set queue size first")

    def update_status(self, message):
        if self.queue:
            size = self.queue.size()
            self.status_label.config(text=f"{message} | Current size: {size}")
        else:
            self.status_label.config(text=message)

    def draw_queue(self):
        self.canvas.delete("all")
        if self.queue:
            x_start = 50
            y_start = 50
            box_width = 50
            box_height = 30
            padding = 10
            for idx, element in enumerate(self.queue.elements):
                x = x_start + idx * (box_width + padding)
                self.canvas.create_rectangle(x, y_start, x + box_width, y_start + box_height, fill="lightblue")
                self.canvas.create_text(x + box_width / 2, y_start + box_height / 2, text=element, font=("Arial", 12))
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

if __name__ == "__main__":
    root = Tk()
    app = QueueApp(root)
    root.mainloop()
