#Practical No.2
#AIM: Stack with insertion, deletion, traversal operations

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Stack Data Structure")
root.state("zoomed")
root['bg']='light blue'

# Configuring row and column
root.columnconfigure((0, 1, 2, 3, 4, 5), weight=10)
root.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Stack size input
size_label = Label(root, text="Enter stack size:")
size_label.grid(row=0, column=0, ipadx=6, ipady=6, padx=10, sticky=E)

size_entry = Entry(root)
size_entry.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, sticky=W)

# Stack operations input
input_label = Label(root, text="Enter the number:")
input_label.grid(row=1, column=0, ipadx=7, ipady=7, padx=10, sticky=E)

input_entry = Entry(root)
input_entry.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, sticky=W)

push_button = Button(root, text="Push", command=lambda: push())
push_button.grid(row=1, column=2, ipadx=5, ipady=5, padx=5, sticky=W)

pop_button = Button(root, text="Pop", command=lambda: pop())
pop_button.grid(row=1, column=3, ipadx=5, ipady=5, padx=5, sticky=W)

peek_button = Button(root, text="Peek", command=lambda: peek())
peek_button.grid(row=1, column=4, ipadx=5, ipady=5, padx=5, sticky=W)

is_empty_button = Button(root, text="Is Empty", command=lambda: is_empty())
is_empty_button.grid(row=1, column=5, ipadx=5, ipady=5, padx=5, sticky=W)

canvas = Canvas(root, width=600, height=400, bg='white')
canvas.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

stack = []
stack_items = []
stack_top = 0
stack_size = 5
item_height = 20

def draw_stack():
    canvas.delete("all")
    y = 400
    for item in stack:
        canvas.create_rectangle(200, y - item_height, 400, y, fill="lightblue")
        canvas.create_text(300, y - item_height // 2, text=item, font=("Helvetica", 16))
        y -= item_height

def set_stack_size():
    global stack_size
    try:
        stack_size = int(size_entry.get())
        if stack_size <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for stack size")

def push():
    global stack_top
    if stack_top < stack_size:
        item = input_entry.get()
        if item:
            stack.append(item)
            input_entry.delete(0, END)
            draw_stack()
            stack_top += 1
        else:
            messagebox.showwarning("Warning", "Please enter a number")
    else:
        messagebox.showwarning("Warning", "Stack Overflow")

def pop():
    global stack_top
    if stack:
        stack.pop()
        draw_stack()
        stack_top -= 1
    else:
        messagebox.showwarning("Warning", "Stack Underflow")

def peek():
    if stack:
        top_item = stack[-1]
        messagebox.showinfo("Peek", f"Top item: {top_item}")
    else:
        messagebox.showwarning("Warning", "Stack is empty")

def is_empty():
    if stack:
        messagebox.showinfo("Is Empty", "Stack is not empty")
    else:
        messagebox.showinfo("Is Empty", "Stack is empty")

# Add a button to set the stack size
set_size_button = Button(root, text="Set Stack Size", command=set_stack_size)
set_size_button.grid(row=0, column=2, ipadx=5, ipady=5, padx=5, sticky=W)

root.mainloop()