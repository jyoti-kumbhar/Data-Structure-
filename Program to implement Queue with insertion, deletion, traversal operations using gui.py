from tkinter import *
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    
    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
        
    def traverse(self):
        if self.is_empty():
            return []
        else:
            return self.elements

class QueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Data Structure")
        self.root.state("zoomed")
        self.root.configure(bg='light blue')

        # Create GUI elements
        self.label = Label(root, text="Queue Data Structure", font=("Arial", 20), bg="light blue")
        self.label.grid(row=0, column=0, columnspan=6, pady=10)

        self.entry_label = Label(self.root, text="Enter element:", font=("Arial", 14), bg="light blue")
        self.entry_label.grid(row=1, column=0, padx=10, pady=10)

        self.entry = Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=1, column=1, padx=10, pady=10)

        self.enqueue_button = Button(self.root, text="Enqueue", font=("Arial", 14), command=self.enqueue_element)
        self.enqueue_button.grid(row=1, column=2, padx=10, pady=10)

        self.dequeue_button = Button(self.root, text="Dequeue", font=("Arial", 14), command=self.dequeue_element)
        self.dequeue_button.grid(row=1, column=3, padx=10, pady=10)

        self.traverse_button = Button(self.root, text="Traverse", font=("Arial", 14), command=self.traverse_queue)
        self.traverse_button.grid(row=1, column=4, padx=10, pady=10)

        self.status_label = Label(self.root, text="", font=("Arial", 14), bg="light blue")
        self.status_label.grid(row=2, column=0, columnspan=6, pady=10)

        # Add a frame to display the queue with a scrollbar
        self.queue_frame = Frame(self.root, bg="white")
        self.queue_frame.grid(row=3, column=0, columnspan=6, pady=10, sticky="nsew")

        self.canvas = Canvas(self.queue_frame, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.queue_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=BOTTOM, fill=X)

        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.queue = Queue()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def enqueue_element(self):
        data = self.entry.get().strip()
        if data:
            self.queue.enqueue(data)
            self.entry.delete(0, END)
            self.update_status(f"Enqueued: {data}")
            self.draw_queue()
        else:
            messagebox.showwarning("Warning", "Element cannot be empty")

    def dequeue_element(self):
        try:
            data = self.queue.dequeue()
            self.update_status(f"Dequeued: {data}")
            self.draw_queue()
        except IndexError:
            messagebox.showwarning("Warning", "Queue is empty")

    def traverse_queue(self):
        elements = self.queue.traverse()
        if elements:
            self.update_status(f"Queue elements: {' -> '.join(elements)}")
        else:
            self.update_status("Queue is empty")
        self.draw_queue()

    def update_status(self, message):
        self.status_label.config(text=message)

    def draw_queue(self):
        self.canvas.delete("all")
        if not self.queue.is_empty():
            x_start = 50
            y_start = 50
            box_width = 100
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
