import tkinter as tk
from tkinter import scrolledtext
import random
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque, defaultdict, Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import heapq
from itertools import permutations
import math

##Stack.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack GUI")
        self.root.configure(bg="light pink")

        self.main_frame = tk.Frame(root, padx=20, pady=20, background='light pink')
        self.main_frame.pack()

        bg="light pink"

        self.entry_label = tk.Label(self.main_frame, text=" Enter Element: ", font=("Arial", 20), bg=bg)
        self.entry_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry = tk.Entry(self.main_frame, width=20, font=("Arial", 20))
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.push_button = tk.Button(self.main_frame, text="Push", width=10, command=self.push_element, font=("Arial", 20))
        self.push_button.grid(row=0, column=2, padx=10, pady=5)

        self.pop_button = tk.Button(self.main_frame, text="Pop", width=10, command=self.pop_element, font=("Arial", 20))
        self.pop_button.grid(row=0, column=3, padx=10, pady=5)

        self.peek_button = tk.Button(self.main_frame, text="Peek", width=10, command=self.peek_element, font=("Arial", 20))
        self.peek_button.grid(row=0, column=4, padx=10, pady=5)

        self.size_button = tk.Button(self.main_frame, text="Size", width=10, command=self.stack_size, font=("Arial", 20))
        self.size_button.grid(row=0, column=5, padx=10, pady=5)

        self.stack_contents_label = tk.Label(self.main_frame, text=" Stack Contents: ", font=("Arial", 20), bg="light pink")
        self.stack_contents_label.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

        self.stack_contents_text = tk.Text(self.main_frame, height=10, width=80, font=("Arial", 20))
        self.stack_contents_text.grid(row=2, column=0, columnspan=5, padx=10, pady=5)

        self.status_text = tk.Text(self.main_frame, height=2, width=80, font=("Arial", 18), state=tk.DISABLED)
        self.status_text.grid(row=3, column=0, columnspan=5, padx=10, pady=5)

        self.stack = Stack()

    def push_element(self):
        element = self.entry.get()
        if element:
            self.stack.push(element)
            self.update_stack_contents()
            self.entry.delete(0, tk.END)  # Clear entry after pushing
            self.update_status(f"Enqueued element: {element}")
        else:
            self.update_status("Warning: Please enter an element.")

    def pop_element(self):
        element = self.stack.pop()
        if element is not None:
            self.update_stack_contents()
            self.update_status(f"Popped element: {element}")
        else:
            self.update_status("Warning: Stack is empty, cannot pop.")

    def peek_element(self):
        element = self.stack.peek()
        if element is not None:
            self.update_status(f"Top element: {element}")
        else:
            self.update_status("Warning: Stack is empty, cannot peek.")

    def stack_size(self):
        size = self.stack.size()
        self.update_status(f"Stack size: {size}")

    def update_stack_contents(self):
        stack_elements = self.stack.display()
        self.stack_contents_text.delete(1.0, tk.END)
        for element in stack_elements[::-1]:
            self.stack_contents_text.insert(tk.END, f"{element}\n")

    def update_status(self, message):
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, message)
        self.status_text.configure(state=tk.DISABLED)

##QUEUE.
class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.pop(0) if self.elements else None

    def peek(self):
        return self.elements[0] if self.elements else None

    def size(self):
        return len(self.elements)

    def display(self):
        return self.elements

class QueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue GUI")
        self.root.configure(bg="light pink")
        self.queue = Queue()
        self.setup_gui()

    def setup_gui(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20, background='light pink')
        self.main_frame.pack()

        self.entry_label = tk.Label(self.main_frame, text=" Enter Element: ", font=("Arial", 20), bg="light pink")
        self.entry_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry = tk.Entry(self.main_frame, width=20, font=("Arial", 20))
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.enqueue_button = tk.Button(self.main_frame, text="Enqueue", width=10, command=self.enqueue_element, font=("Arial", 20))
        self.enqueue_button.grid(row=0, column=2, padx=10, pady=5)

        self.dequeue_button = tk.Button(self.main_frame, text="Dequeue", width=10, command=self.dequeue_element, font=("Arial", 20))
        self.dequeue_button.grid(row=0, column=3, padx=10, pady=5)

        self.peek_button = tk.Button(self.main_frame, text="Peek", width=10, command=self.peek_element, font=("Arial", 20))
        self.peek_button.grid(row=0, column=4, padx=10, pady=5)

        self.size_button = tk.Button(self.main_frame, text="Size", width=10, command=self.queue_size, font=("Arial", 20))
        self.size_button.grid(row=0, column=5, padx=10, pady=5)

        self.queue_contents_label = tk.Label(self.main_frame, text=" Queue Contents: ", font=("Arial", 20), bg="light pink")
        self.queue_contents_label.grid(row=3, column=0, columnspan=5, padx=10, pady=5)

        self.queue_contents_text = tk.Text(self.main_frame, height=10, width=80, font=("Arial", 20))
        self.queue_contents_text.grid(row=4, column=0, columnspan=5, padx=10, pady=5)

        self.status_text = tk.Text(self.main_frame, height=2, width=80, font=("Arial", 18), state=tk.DISABLED)
        self.status_text.grid(row=5, column=0, columnspan=5, padx=10, pady=5)

    def enqueue_element(self):
        element = self.entry.get()
        if element:
            self.queue.enqueue(element)
            self.update_queue_contents()
            self.entry.delete(0, tk.END)
            self.update_status(f"Enqueued element: {element}")
        else:
            self.update_status("Warning: Please enter an element.")

    def dequeue_element(self):
        element = self.queue.dequeue()
        if element is not None:
            self.update_queue_contents()
            self.update_status(f"Dequeued element: {element}")
        else:
            self.update_status("Warning: Queue is empty, cannot dequeue.")

    def peek_element(self):
        element = self.queue.peek()
        if element is not None:
            self.update_status(f"Front element: {element}")
        else:
            self.update_status("Warning: Queue is empty, cannot peek.")

    def queue_size(self):
        size = self.queue.size()
        self.update_status(f"Queue size: {size}")

    def update_queue_contents(self):
        queue_elements = self.queue.display()
        self.queue_contents_text.delete(1.0, tk.END)
        for element in queue_elements:
            self.queue_contents_text.insert(tk.END, f"{element}\n")

    def update_status(self, message):
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, message)
        self.status_text.configure(state=tk.DISABLED)
# Priority Queue GUI.

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data, priority):
        self.items.append((data, priority))
        self.items.sort(key=lambda x: x[1])  # Sort by priority

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)[0]  # Return the element with the highest priority

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0][0]  # Peek at the element with the highest priority

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

class PriorityQueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Priority Queue GUI")
        self.root.configure(bg="light pink")
        self.priority_queue = PriorityQueue()
        self.setup_gui()

    def setup_gui(self):
        self.main_frame = tk.Frame(self.root, padx=20, pady=20, background='light pink')
        self.main_frame.pack()

        # Entry for Element
        self.entry_label = tk.Label(self.main_frame, text=" Enter Element: ", font=("Arial", 20), bg="light pink")
        self.entry_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry = tk.Entry(self.main_frame, width=20, font=("Arial", 20))
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for Priority
        self.priority_label = tk.Label(self.main_frame, text=" Priority: ", font=("Arial", 20), bg="light pink")
        self.priority_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.priority_entry = tk.Entry(self.main_frame, width=20, font=("Arial", 20))
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5)

        # Enqueue Button
        self.enqueue_button = tk.Button(self.main_frame, text="Enqueue", width=10, command=self.enqueue_element, font=("Arial", 20),bg="light pink")
        self.enqueue_button.grid(row=0, column=2, padx=10, pady=5)

        # Dequeue Button
        self.dequeue_button = tk.Button(self.main_frame, text="Dequeue", width=10, command=self.dequeue_element, font=("Arial", 20),bg="light pink")
        self.dequeue_button.grid(row=0, column=3, padx=10, pady=5)

        # Peek Button
        self.peek_button = tk.Button(self.main_frame, text="Peek", width=10, command=self.peek_element, font=("Arial", 20),bg="light pink")
        self.peek_button.grid(row=1, column=2, padx=10, pady=5)

        # Size Button
        self.size_button = tk.Button(self.main_frame, text="Size", width=10, command=self.priority_queue_size, font=("Arial", 20),bg="light pink")
        self.size_button.grid(row=1, column=3, padx=10, pady=5)

        # Priority Queue Contents Label
        self.queue_contents_label = tk.Label(self.main_frame, text=" Priority Queue Contents: ", font=("Arial", 20), bg="light pink")
        self.queue_contents_label.grid(row=2, column=0, columnspan=5, padx=10, pady=5)

        # Text area to display the Priority Queue
        self.queue_contents_text = tk.Text(self.main_frame, height=10, width=80, font=("Arial", 20))
        self.queue_contents_text.grid(row=5, column=0, columnspan=5, padx=10, pady=5)

        # Status text area
        self.status_text = tk.Text(self.main_frame, height=2, width=80, font=("Arial", 18), state=tk.DISABLED)
        self.status_text.grid(row=6, column=0, columnspan=5, padx=10, pady=5)

    def enqueue_element(self):
        element = self.entry.get()
        try:
            priority = int(self.priority_entry.get())
            if element:
                self.priority_queue.enqueue(element, priority)
                self.update_queue_contents()
                self.entry.delete(0, tk.END)
                self.priority_entry.delete(0, tk.END)
                self.update_status(f"Enqueued: {element} with priority {priority}")
            else:
                self.update_status("Warning: Please enter an element.")
        except ValueError:
            self.update_status("Warning: Please enter a valid priority (integer).")

    def dequeue_element(self):
        element = self.priority_queue.dequeue()
        if element is not None:
            self.update_queue_contents()
            self.update_status(f"Dequeued element: {element}")
        else:
            self.update_status("Warning: Priority Queue is empty, cannot dequeue.")

    def peek_element(self):
        element = self.priority_queue.peek()
        if element is not None:
            self.update_status(f"Top element: {element}")
        else:
            self.update_status("Warning: Priority Queue is empty, cannot peek.")

    def priority_queue_size(self):
        size = self.priority_queue.size()
        self.update_status(f"Priority Queue size: {size}")

    def update_queue_contents(self):
        queue_elements = self.priority_queue.display()
        self.queue_contents_text.delete(1.0, tk.END)
        for element in queue_elements:
            self.queue_contents_text.insert(tk.END, f"{element[0]} (Priority: {element[1]})\n")

    def update_status(self, message):
        self.status_text.configure(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, message)
        self.status_text.configure(state=tk.DISABLED)

# Singly Linked List class.
class SLLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Singly Linked List.
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        temp = self.head

        # If the head node itself holds the key to be deleted.
        if temp is not None and temp.data == data:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted.
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        # If the key was not present in the linked list.
        if temp is None:
            return

        # Unlink the node from the linked list.
        prev.next = temp.next
        temp = None

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Singly linked List GUI.
class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List GUI")
        self.root.configure(bg="light pink")
        self.root.state("zoomed")

        self.linked_list = LinkedList()

        # Label for entry
        self.label = tk.Label(root, text="Enter Value:", bg="light pink", font=("Arial", 20))
        self.label.pack(pady=10)

        # Entry box for input
        self.entry = tk.Entry(root, font=("Arial", 20), width=30)
        self.entry.pack(pady=5)

        # Insert button
        self.insert_button = tk.Button(root, text="  Insert  ", command=self.insert_value, bg="light pink", font=("Arial", 20))
        self.insert_button.pack(pady=5)

        # Delete button
        self.delete_button = tk.Button(root, text="  Delete  ", command=self.delete_value, bg="light pink", font=("Arial", 20))
        self.delete_button.pack(pady=5)

        # Traverse button
        self.traverse_button = tk.Button(root, text=" Traverse ", command=self.traverse_list, bg="light pink", font=("Arial", 20))
        self.traverse_button.pack(pady=5)

        # Result label to display list
        self.result_label = tk.Label(root, text="List: []", bg="light pink", font=("Arial", 20))
        self.result_label.pack(pady=10)

        # Status text area
        self.status_text = tk.Text(root, height=2, width=50, font=("Arial", 18), state=tk.DISABLED)
        self.status_text.pack(pady=10)

    def insert_value(self):
        """Insert value into the linked list."""
        value = self.entry.get()
        if value:
            self.linked_list.insert(value)
            self.update_status(f"Inserted {value} into the list")
            self.entry.delete(0, tk.END)  # Clear the entry box.

    def delete_value(self):
        """Delete value from the linked list."""
        value = self.entry.get()
        if value:
            self.linked_list.delete(value)
            self.update_status(f"Deleted {value} from the list")
            self.entry.delete(0, tk.END)  # Clear the entry box.

    def traverse_list(self):
        """Traverse the linked list and display the elements."""
        elements = self.linked_list.traverse()
        self.result_label.config(text="List: " + " -> ".join(elements))

    def update_status(self, message):
        """Update the status text area."""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, message)
        self.status_text.config(state=tk.DISABLED)

# Node for Doubly Linked List.
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        deleted_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node.data

# Doubly Linked List GUI.
class DoublyLinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List Operations")
        self.root.configure(bg="light pink")
        self.root.state("zoomed")

        self.doubly_linked_list = DoublyLinkedList()

        self.root.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.root.grid_columnconfigure((0,1,2,3,4), weight=10)

        # Label for output
        self.label_output = tk.Label(root, text="Doubly Linked List:", bg="light pink", font=("Arial", 20))
        self.label_output.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # Entry widget for inserting elements
        self.entry_insert = tk.Entry(root, width=20, font=("Arial", 20))
        self.entry_insert.grid(row=0, column=1, padx=10, pady=10)

        # Buttons for insert operations
        self.button_insert_beginning = tk.Button(root, text="Insert at Beginning", bg="light pink", font=("Arial", 20), command=self.insert_at_beginning)
        self.button_insert_beginning.grid(row=0, column=2, padx=10, pady=10)

        self.button_insert_end = tk.Button(root, text="Insert at End", bg="light pink", font=("Arial", 20), command=self.insert_at_end)
        self.button_insert_end.grid(row=0, column=3, padx=10, pady=10)

        # Button for delete operations
        self.button_delete_beginning = tk.Button(root, text="Delete from Beginning", bg="light pink", font=("Arial", 20), command=self.delete_from_beginning)
        self.button_delete_beginning.grid(row=1, column=2, padx=10, pady=10)

        self.button_delete_end = tk.Button(root, text="Delete from End", bg="light pink", font=("Arial", 20), command=self.delete_from_end)
        self.button_delete_end.grid(row=1, column=3, padx=10, pady=10)

        # Text widget to display the doubly linked list
        self.text_output = tk.Text(root, height=10, width=80, font=("Arial", 20))
        self.text_output.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Status text area
        self.status_text = tk.Text(root, height=2, width=80, font=("Arial", 18), state=tk.DISABLED, background="light pink")
        self.status_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def insert_at_beginning(self):
        try:
            data = int(self.entry_insert.get())
            self.doubly_linked_list.insert_at_beginning(data)
            self.update_output()
            self.entry_insert.delete(0, tk.END)
            self.update_status(f"Inserted {data} at the beginning.")
        except ValueError:
            self.update_status("Error: Please enter a valid integer.")

    def insert_at_end(self):
        try:
            data = int(self.entry_insert.get())
            self.doubly_linked_list.insert_at_end(data)
            self.update_output()
            self.entry_insert.delete(0, tk.END)
            self.update_status(f"Inserted {data} at the end.")
        except ValueError:
            self.update_status("Error: Please enter a valid integer.")

    def delete_from_beginning(self):
        deleted_data = self.doubly_linked_list.delete_at_beginning()
        if deleted_data is not None:
            self.update_output()
            self.update_status(f"Deleted {deleted_data} from the beginning.")
        else:
            self.update_status("Warning: The list is empty.")

    def delete_from_end(self):
        deleted_data = self.doubly_linked_list.delete_at_end()
        if deleted_data is not None:
            self.update_output()
            self.update_status(f"Deleted {deleted_data} from the end.")
        else:
            self.update_status("Warning: The list is empty.")

    def update_output(self):
        self.text_output.delete(1.0, tk.END)
        current = self.doubly_linked_list.head
        while current:
            self.text_output.insert(tk.END, str(current.data) + " <-> ")
            current = current.next
        self.text_output.insert(tk.END, "None")

    def update_status(self, message):
        """Update the status text area."""
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, message)
        self.status_text.config(state=tk.DISABLED)

# Binary Tree Node.
class BTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Binary Tree.
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = BTNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = BTNode(key)
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

# GUI for Binary Tree.
class BinaryTreeGUI:
    def __init__(self, tree):
        self.tree = tree
        self.window = tk.Tk()
        self.window.title("Binary Tree GUI")
        self.window.state("zoomed")
        self.window.configure(bg="light pink")

        # Title label
        self.label = tk.Label(self.window, bg="light pink", text="Binary Tree GUI", font=("Arial", 20))
        self.label.pack(pady=10)

        # Frame for entry and label
        self.entry_frame = tk.Frame(self.window, bg='light pink')
        self.entry_frame.pack(pady=10)

        # Input fields
        self.label = tk.Label(self.entry_frame, bg="light pink", text="Enter a value:", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10)
        self.entry = tk.Entry(self.entry_frame, font=("Arial", 20))
        self.entry.grid(row=0, column=1, padx=10)

        # Frame for buttons
        self.button_frame = tk.Frame(self.window, bg="light pink")
        self.button_frame.pack(pady=10)

        # Buttons
        self.insert_button = tk.Button(self.button_frame, text="Insert", font=("Arial", 20), command=self.insert_value)
        self.insert_button.grid(row=1, column=0, padx=5, pady=5)
        self.delete_button = tk.Button(self.button_frame, text="Delete", font=("Arial", 20), command=self.delete_value)
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)
        self.inorder_button = tk.Button(self.button_frame, text="Inorder Traversal", font=("Arial", 20), command=self.show_inorder)
        self.inorder_button.grid(row=2, column=0, padx=5, pady=5)
        self.preorder_button = tk.Button(self.button_frame, text="Preorder Traversal", font=("Arial", 20), command=self.show_preorder)
        self.preorder_button.grid(row=2, column=1, padx=5, pady=5)
        self.postorder_button = tk.Button(self.button_frame, text="Postorder Traversal", font=("Arial", 20), command=self.show_postorder)
        self.postorder_button.grid(row=2, column=2, padx=5, pady=5)

        # Canvas for tree drawing
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack(pady=10)

        # Text area for status and results
        self.text_area = tk.Text(self.window, height=5, width=60, font=("Arial", 18), state=tk.DISABLED)
        self.text_area.pack(pady=10)

        self.window.mainloop()

    def insert_value(self):
        try:
            value = int(self.entry.get())
            self.tree.insert(value)
            self.update_text_area(f"Inserted {value}")
        except ValueError:
            self.update_text_area("Error: Please enter a valid integer.")
        self.draw_tree()

    def delete_value(self):
        try:
            value = int(self.entry.get())
            self.tree.delete(value)
            self.update_text_area(f"Deleted {value}")
        except ValueError:
            self.update_text_area("Error: Please enter a valid integer.")
        self.draw_tree()

    def show_inorder(self):
        result = self.tree.inorder_traversal()
        self.update_text_area(f"Inorder Traversal: {result}")
        self.draw_tree()

    def show_preorder(self):
        result = self.tree.preorder_traversal()
        self.update_text_area(f"Preorder Traversal: {result}")
        self.draw_tree()

    def show_postorder(self):
        result = self.tree.postorder_traversal()
        self.update_text_area(f"Postorder Traversal: {result}")
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        if self.tree.root is not None:
            self._draw_tree(self.tree.root, 300, 20, 100)

    def _draw_tree(self, node, x, y, dx):
        if node is None:
            return
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill='light pink', outline='black')
        self.canvas.create_text(x, y, text=str(node.val))
        if node.left is not None:
            self.canvas.create_line(x, y, x-dx, y+50, fill='black')
            self._draw_tree(node.left, x-dx, y+50, dx/2)
        if node.right is not None:
            self.canvas.create_line(x, y, x+dx, y+50, fill='black')
            self._draw_tree(node.right, x+dx, y+50, dx/2)

    def update_text_area(self, message):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, message)
        self.text_area.config(state=tk.DISABLED)

# Huffman Tree.
class HuffmanNode:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}, None

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)

    return encoded_data, codebook, root

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""

    return decoded_data

def draw_tree(canvas, node, x, y, dx):
    if node is None:
        return

    if node.left is not None:
        canvas.create_line(x, y, x - dx, y + 50, fill="black")
        draw_tree(canvas, node.left, x - dx, y + 50, dx / 2)

    if node.right is not None:
        canvas.create_line(x, y, x + dx, y + 50, fill="black")
        draw_tree(canvas, node.right, x + dx, y + 50, dx / 2)

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="light pink", outline="black")
    canvas.create_text(x, y, text=f"{node.char if node.char is not None else ''}\n{node.freq}", anchor="center", fill="black")

# Huffman GUI.
class HuffmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding GUI")
        self.root.state("zoomed")
        self.root.configure(bg="light pink")

        # Create a canvas and a scrollbar for the entire window
        self.canvas = tk.Canvas(root, bg="light pink")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a frame to hold all the widgets
        self.frame = tk.Frame(self.canvas, bg="light pink")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Bind the frame size change to update canvas scroll region
        self.frame.bind("<Configure>", self.on_frame_configure)
                
        self.root.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.root.grid_columnconfigure((0,1,2,3,4,5,6), weight=10)
        # Input data
        tk.Label(self.frame, bg="light pink", text="Enter Your Data:", font=("Arial", 20)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.data_entry = tk.Entry(self.frame, width=50, font=("Arial", 20))
        self.data_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Encode button
        tk.Button(self.frame, bg="light pink", text="Encode", font=("Arial", 20), command=self.encode_data).grid(row=1, column=2, padx=10, pady=5, sticky="w")

        # Size comparison
        tk.Label(self.frame, bg="light pink", text="Original Size:", font=("Arial", 20)).grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.original_size_label = tk.Label(self.frame, bg="light pink", text="", font=("Arial", 20))
        self.original_size_label.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        tk.Label(self.frame, bg="light pink", fg="black", text="Compressed Size:", font=("Arial", 20)).grid(row=4, column=2, padx=10, pady=5, sticky="e")
        self.compressed_size_label = tk.Label(self.frame, bg="light pink", text="", font=("Arial", 20))
        self.compressed_size_label.grid(row=4, column=3, padx=10, pady=5, sticky="w")

        # Encoded data
        tk.Label(self.frame, bg="light pink", text="Encoded Data:", font=("Arial", 20)).grid(row=3, column=0, padx=10, pady=5, sticky="ne")
        self.encoded_frame = tk.Frame(self.frame)
        self.encoded_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.encoded_text = scrolledtext.ScrolledText(self.encoded_frame, height=2, width=50, font=("Arial", 20))
        self.encoded_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.encoded_scrollbar = tk.Scrollbar(self.encoded_frame, command=self.encoded_text.yview)
        self.encoded_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.encoded_text.config(yscrollcommand=self.encoded_scrollbar.set)

        # Codebook
        tk.Label(self.frame, bg="light pink", text="Codebook:", font=("Arial", 20)).grid(row=4, column=0, padx=10, pady=5, sticky="ne")
        self.codebook_frame = tk.Frame(self.frame)
        self.codebook_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.codebook_text = scrolledtext.ScrolledText(self.codebook_frame, height=2, width=50, font=("Arial", 20))
        self.codebook_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.codebook_scrollbar = tk.Scrollbar(self.codebook_frame, command=self.codebook_text.yview)
        self.codebook_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.codebook_text.config(yscrollcommand=self.codebook_scrollbar.set)

        # Huffman Tree Canvas
        tk.Label(self.frame, bg="light pink", text="Huffman Tree:", font=("Arial", 20)).grid(row=5, column=0, padx=10, pady=5, sticky="ne")
        self.tree_canvas = tk.Canvas(self.frame, width=500, height=300)
        self.tree_canvas.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Decode button
        tk.Button(self.frame, bg="light pink", text="Decode", font=("Arial", 20), command=self.decode_data).grid(row=7, column=2, padx=10, pady=5, sticky="w")

        # Decoded data
        tk.Label(self.frame, bg="light pink", text="Decoded Data:", font=("Arial", 20)).grid(row=7, column=0, padx=10, pady=5, sticky="ne")
        self.decoded_frame = tk.Frame(self.frame)
        self.decoded_frame.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.decoded_text = scrolledtext.ScrolledText(self.decoded_frame, height=5, width=50, font=("Arial", 20))
        self.decoded_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.decoded_scrollbar = tk.Scrollbar(self.decoded_frame, command=self.decoded_text.yview)
        self.decoded_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.decoded_text.config(yscrollcommand=self.decoded_scrollbar.set)

        

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def encode_data(self):
        data = self.data_entry.get()
        encoded_data, codebook, root = huffman_encoding(data)
        self.encoded_text.delete(1.0, tk.END)
        self.encoded_text.insert(tk.END, encoded_data)
        self.codebook_text.delete(1.0, tk.END)
        self.codebook_text.insert(tk.END, str(codebook))

        self.tree_canvas.delete("all")
        draw_tree(self.tree_canvas, root, x=250, y=30, dx=100)

        original_size = len(data) * 8  # Assuming each character is 1 byte
        compressed_size = len(encoded_data)
        self.original_size_label.config(text=f"{original_size} bits")
        self.compressed_size_label.config(text=f"{compressed_size} bits")

        self.encoded_data = encoded_data
        self.codebook = codebook

    def decode_data(self):
        decoded_data = huffman_decoding(self.encoded_data, self.codebook)
        self.decoded_text.delete(1.0, tk.END)
        self.decoded_text.insert(tk.END, decoded_data)
        

#Graph.
class Graph:
    def __init__(self):
        self.graph = {}
        self.positions = {}  # Store positions of vertices for drawing

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in list(self.graph[vertex]):
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]
            if vertex in self.positions:
                del self.positions[vertex]
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
            return True
        else:
            return False

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Graph GUI.
class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Operations")
        self.root.state('zoomed')
        self.root.configure(bg="light pink")

        # Create a canvas and a frame inside it for the main content
        self.canvas = tk.Canvas(root, bg="light pink")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a vertical scrollbar for the main window
        self.v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the vertical scrollbar
        self.canvas.config(yscrollcommand=self.v_scrollbar.set)

        # Frame inside the canvas
        self.canvas_frame = tk.Frame(self.canvas, bg="light pink")
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        # Bind the frame configuration to update canvas scrollregion
        self.canvas_frame.bind("<Configure>", self.on_frame_configure)

        # Initialize graph and widgets
        self.graph = Graph()
        self.init_widgets()

    def init_widgets(self):
        # Vertex Input
        self.vertex_label = tk.Label(self.canvas_frame, text="Vertex:", font=("Arial", 20),bg="light pink")
        self.vertex_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.vertex_entry = tk.Entry(self.canvas_frame, font=("Arial", 20))
        self.vertex_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.add_vertex_button = tk.Button(self.canvas_frame, text="    Add Vertex   ", font=("Arial", 20) ,bg="light pink", command=self.add_vertex)
        self.add_vertex_button.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

        self.remove_vertex_button = tk.Button(self.canvas_frame, text="Remove Vertex", font=("Arial", 20), background='light pink', command=self.remove_vertex)
        self.remove_vertex_button.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

        # Edge Input
        self.vertex1_label = tk.Label(self.canvas_frame, text="Vertex 1:", font=("Arial", 20), bg="light pink")
        self.vertex1_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.vertex1_entry = tk.Entry(self.canvas_frame, font=("Arial", 20))
        self.vertex1_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.vertex2_label = tk.Label(self.canvas_frame, text="Vertex 2:", font=("Arial", 20), bg="light pink")
        self.vertex2_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.vertex2_entry = tk.Entry(self.canvas_frame, font=("Arial", 20))
        self.vertex2_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.add_edge_button = tk.Button(self.canvas_frame, text="    Add Edge     ", font=("Arial", 20), bg="light pink", command=self.add_edge)
        self.add_edge_button.grid(row=3, column=1, padx=10, pady=5, columnspan=2)
        self.remove_edge_button = tk.Button(self.canvas_frame, text=" Remove Edge ", font=("Arial", 20),bg="light pink", command=self.remove_edge)
        self.remove_edge_button.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

        # Display Graph
        self.display_button = tk.Button(self.canvas_frame, text=" Display Graph ", font=("Arial", 20), bg="light pink",command=self.display_graph)
        self.display_button.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        # Output Text and Scrollbar
        self.output_frame = tk.Frame(self.canvas_frame)
        self.output_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        self.output_text = tk.Text(self.output_frame, height=10, width=50, font=("Arial", 20))
        self.output_text.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        self.scrollbar = tk.Scrollbar(self.output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output_text.config(yscrollcommand=self.scrollbar.set)

        # Canvas for Drawing
        self.canvas_draw_frame = tk.Frame(self.canvas_frame)
        self.canvas_draw_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        self.draw_canvas = tk.Canvas(self.canvas_draw_frame, width=1400, height=750)
        self.draw_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.x_scrollbar = tk.Scrollbar(self.canvas_draw_frame, orient=tk.HORIZONTAL, command=self.draw_canvas.xview)
        self.x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.y_scrollbar = tk.Scrollbar(self.canvas_draw_frame, orient=tk.VERTICAL, command=self.draw_canvas.yview)
        self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.draw_canvas.config(xscrollcommand=self.x_scrollbar.set, yscrollcommand=self.y_scrollbar.set)

    def on_frame_configure(self, event):
        """Update the scroll region of the canvas when the frame is resized."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            if self.graph.add_vertex(vertex):
                x, y = self.random_position()
                self.graph.positions[vertex] = (x, y)
                self.draw_graph()
                self.output_text.insert(tk.END, f"Added vertex: {vertex}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a vertex.\n")

    def remove_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            if self.graph.remove_vertex(vertex):
                self.draw_graph()
                self.output_text.insert(tk.END, f"Removed vertex: {vertex}\n")
            else:
                self.output_text.insert(tk.END, "Input Error: Vertex does not exist.\n")
            self.vertex_entry.delete(0, tk.END)
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a vertex.\n")

    def add_edge(self):
        vertex1 = self.vertex1_entry.get()
        vertex2 = self.vertex2_entry.get()
        if vertex1 and vertex2:
            if self.graph.add_edge(vertex1, vertex2):
                self.draw_graph()
                self.output_text.insert(tk.END, f"Added edge: {vertex1} - {vertex2}\n")
            else:
                self.output_text.insert(tk.END, "Input Error: One or both vertices do not exist.\n")
            self.vertex1_entry.delete(0, tk.END)
            self.vertex2_entry.delete(0, tk.END)
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter both vertices.\n")

    def remove_edge(self):
        vertex1 = self.vertex1_entry.get()
        vertex2 = self.vertex2_entry.get()
        if vertex1 and vertex2:
            if self.graph.remove_edge(vertex1, vertex2):
                self.draw_graph()
                self.output_text.insert(tk.END, f"Removed edge: {vertex1} - {vertex2}\n")
            else:
                self.output_text.insert(tk.END, "Input Error: Edge does not exist.\n")
            self.vertex1_entry.delete(0, tk.END)
            self.vertex2_entry.delete(0, tk.END)
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter both vertices.\n")

    def display_graph(self):
        self.output_text.delete(1.0, tk.END)
        for vertex, edges in self.graph.graph.items():
            self.output_text.insert(tk.END, f"{vertex}: {edges}\n")

    def random_position(self):
        """Generate random (x, y) coordinates for vertex placement."""
        import random
        x = random.randint(50, 1300)
        y = random.randint(50, 700)
        return x, y

    def draw_graph(self):
        """Draw the graph on the canvas."""
        self.draw_canvas.delete("all")

        # Draw vertices
        for vertex, (x, y) in self.graph.positions.items():
            self.draw_canvas.create_oval(x-20, y-20, x+20, y+20, fill="light pink")
            self.draw_canvas.create_text(x, y, text=vertex, font=("Arial", 16, "bold"))

        # Draw edges
        for vertex, edges in self.graph.graph.items():
            x1, y1 = self.graph.positions[vertex]
            for adjacent in edges:
                x2, y2 = self.graph.positions[adjacent]
                self.draw_canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

# Hash Table.
class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given character key (using ASCII value)."""
        return ord(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def delete(self, key):
        """Delete the value associated with the given character key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

    def search(self, key):
        """Search for the value associated with the given character key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def traverse(self):
        """Traverse and return all key-value pairs in the hash table."""
        result = []
        for index, item in enumerate(self.table):
            if item is not None:
                key, value = item
                result.append(f"Index {index}: Key {key}, Value {value}")
        return result

# BFS Graph.
class BFSGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs_tree(self, start):
        """Perform BFS and return the Breadth-First Tree as a dictionary."""
        visited = set()
        bfs_tree = defaultdict(list)
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_tree[current].append(neighbor)
                    queue.append(neighbor)

        return bfs_tree

    def visualize(self, bfs_tree=None):
        """Visualize the graph and optionally the BFS tree."""
        G = nx.Graph(self.graph)

        pos = nx.spring_layout(G)

        fig, ax = plt.subplots(1, 2, figsize=(12, 6))

        # Draw the original graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
                node_size=1000, font_size=15, font_weight='bold', ax=ax[0])
        ax[0].set_title("Graph")

        # Draw the BFS Tree
        if bfs_tree:
            T = nx.DiGraph(bfs_tree)
            pos_tree = nx.spring_layout(T)
            nx.draw(T, pos_tree, with_labels=True, node_color='lightgreen', edge_color='blue',
                    node_size=1000, font_size=15, font_weight='bold', arrows=True, ax=ax[1])
            ax[1].set_title("BFS Tree")

        return fig

# BFS GUI.
class BFSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph BFS Visualization")
        self.root.state("zoomed")
        self.root.configure(bg="light pink")

        self.graph = BFSGraph()  # Corrected initialization

        # Vertex and Edge Entry
        self.vertex_label = tk.Label(root, text="Vertex:",bg="light pink", font=("Arial", 20))
        self.vertex_label.grid(row=1, column=0, columnspan=1)
        self.vertex_entry = tk.Entry(root, font=("Arial", 20))
        self.vertex_entry.grid(row=1, column=1, columnspan=1)

        self.add_vertex_button = tk.Button(root, text="   Add Vertex   ", bg="light pink", font=("Arial", 20), command=self.add_vertex)
        self.add_vertex_button.grid(row=1, column=4, columnspan=1)

        self.edge_label = tk.Label(root, text="Edge (vertex1 vertex2):", bg="light pink", font=("Arial", 20))
        self.edge_label.grid(row=2, column=0, columnspan=1)
        self.edge_entry = tk.Entry(root, font=("Arial", 20))
        self.edge_entry.grid(row=2, column=1, columnspan=1)

        self.add_edge_button = tk.Button(root, text="     Add Edge    ", bg="light pink" ,font=("Arial", 20), command=self.add_edge)
        self.add_edge_button.grid(row=2, column=4, columnspan=1)

        # Start BFS Entry
        self.bfs_label = tk.Label(root, text="Start Vertex for BFS:", bg="light pink", font=("Arial", 20))
        self.bfs_label.grid(row=3, column=0)
        self.bfs_entry = tk.Entry(root, font=("Arial", 20))
        self.bfs_entry.grid(row=3, column=1)

        self.bfs_button = tk.Button(root, text="  Perform BFS ",bg="light pink" ,font=("Arial", 20), command=self.perform_bfs)
        self.bfs_button.grid(row=3, column=4, columnspan=1)

        self.display_button = tk.Button(root, text=" Display Graph", bg="light pink", font=("Arial", 20), command=self.display_graph)
        self.display_button.grid(row=4, column=4)

        # Canvas for matplotlib graph visualization
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.grid(row=6, column=0, columnspan=3)

        # ScrolledText for output messages
        self.output_text = scrolledtext.ScrolledText(root, height=5, width=60, font=("Arial", 16))
        self.output_text.grid(row=5, column=0, columnspan=2)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Added vertex: {vertex}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a valid vertex.\n")

    def add_edge(self):
        edge = self.edge_entry.get().split()
        if len(edge) == 2:
            vertex1, vertex2 = edge
            self.graph.add_edge(vertex1, vertex2)
            self.edge_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Added edge: {vertex1} - {vertex2}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter two valid vertices.\n")

    def perform_bfs(self):
        start_vertex = self.bfs_entry.get()
        if start_vertex:
            if start_vertex not in self.graph.graph:
                self.output_text.insert(tk.END, f"Input Error: Vertex '{start_vertex}' does not exist.\n")
                return
           
            bfs_tree = self.graph.bfs_tree(start_vertex)
            self.display_graph(bfs_tree)
            self.output_text.insert(tk.END, f"Performed BFS starting from: {start_vertex}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a start vertex for BFS.\n")

    def display_graph(self, bfs_tree=None):
        """Display the graph and BFS tree in the GUI using matplotlib."""
        fig = self.graph.visualize(bfs_tree)

        # Clear the old plot if it exists
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0)

# DFS Graph.
class DFSGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def dfs_tree(self, start):
        """Perform DFS and return the Depth-First Tree as a dictionary."""
        visited = set()
        dfs_tree = defaultdict(list)
       
        def dfs(vertex):
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs_tree[vertex].append(neighbor)
                    dfs(neighbor)

        visited.add(start)
        dfs(start)
       
        return dfs_tree

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def visualize(self, dfs_tree=None):
        """Visualize the graph and optionally the DFS tree."""
        G = nx.Graph(self.graph)

        pos = nx.spring_layout(G)

        fig, ax = plt.subplots(1, 2, figsize=(12, 6))

        # Draw the original graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
                node_size=1000, font_size=15, font_weight='bold', ax=ax[0])
        ax[0].set_title("Graph")

        # Draw the DFS Tree
        if dfs_tree:
            T = nx.DiGraph(dfs_tree)
            pos_tree = nx.spring_layout(T)
            nx.draw(T, pos_tree, with_labels=True, node_color='lightgreen', edge_color='blue',
                    node_size=1000, font_size=15, font_weight='bold', arrows=True, ax=ax[1])
            ax[1].set_title("DFS Tree")

        return fig

# DFS GUI.
class DfSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph DFS Visualization")
        self.root.state("zoomed")
        self.root.configure(bg="light pink")

        self.graph = DFSGraph()

        # Vertex Entry
        self.vertex_label = tk.Label(root, text="Vertex:",bg="light pink", font=("Arial", 20))
        self.vertex_label.grid(row=1, column=0)
        self.vertex_entry = tk.Entry(root, font=("Arial", 20))
        self.vertex_entry.grid(row=1, column=1)

        self.add_vertex_button = tk.Button(root, text="   Add Vertex   ", bg="light pink",font=("Arial", 20), command=self.add_vertex)
        self.add_vertex_button.grid(row=1, column=4)

        # Edge Entry
        self.edge_label = tk.Label(root, text="Edge (vertex1 vertex2):", bg="light pink",
                                   font=("Arial", 20))
        self.edge_label.grid(row=2, column=0)
        self.edge_entry = tk.Entry(root, font=("Arial", 20))
        self.edge_entry.grid(row=2, column=1)

        self.add_edge_button = tk.Button(root, text="     Add Edge    ", bg="light pink",
                                         font=("Arial", 20), command=self.add_edge)
        self.add_edge_button.grid(row=2, column=4)

        # DFS Entry
        self.dfs_label = tk.Label(root, text="Start Vertex for DFS:", bg="light pink",
                                  font=("Arial", 20))
        self.dfs_label.grid(row=3, column=0)
        self.dfs_entry = tk.Entry(root, font=("Arial", 20))
        self.dfs_entry.grid(row=3, column=1)

        self.dfs_button = tk.Button(root, text="  Perform DFS ", bg="light pink",
                                    font=("Arial", 20), command=self.perform_dfs)
        self.dfs_button.grid(row=3, column=4)

        self.display_button = tk.Button(root, text=" Display Graph",bg="light pink",
                                        font=("Arial", 20), command=self.display_graph)
        self.display_button.grid(row=4, column=4)

        # Canvas for matplotlib graph visualization
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.grid(row=6, column=0, columnspan=3)

        # ScrolledText for output messages
        self.output_text = scrolledtext.ScrolledText(root, height=5, width=60, font=("Arial", 16))
        self.output_text.grid(row=5, column=0, columnspan=2)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Added vertex: {vertex}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a valid vertex.\n")

    def add_edge(self):
        edge = self.edge_entry.get().split()
        if len(edge) == 2:
            vertex1, vertex2 = edge
            self.graph.add_edge(vertex1, vertex2)
            self.edge_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Added edge: {vertex1} - {vertex2}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter two valid vertices.\n")

    def perform_dfs(self):
        start_vertex = self.dfs_entry.get()
        if start_vertex:
            if start_vertex not in self.graph.graph:
                self.output_text.insert(tk.END, f"Input Error: Vertex '{start_vertex}' does not exist.\n")
                return
           
            dfs_tree = self.graph.dfs_tree(start_vertex)
            self.display_graph(dfs_tree)
            self.output_text.insert(tk.END, f"Performed DFS starting from: {start_vertex}\n")
        else:
            self.output_text.insert(tk.END, "Input Error: Please enter a start vertex for DFS.\n")

    def display_graph(self, dfs_tree=None):
        """Display the graph and DFS tree in the GUI using matplotlib."""
        fig = self.graph.visualize(dfs_tree)

        # Clear the old plot if it exists
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
# GUI Code
class CollisionGUI:
    def __init__(self, root):
        self.hash_table = HashTable(size=10)
        self.root = root
        self.root.title("Hash Table with Overflow Chaining")
        self.root.state("zoomed")
        self.root.configure(bg="light pink")

        self.frame = tk.Frame(self.root, bg="light pink")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.init_widgets()

    def init_widgets(self):

        # Key and Value Input
        self.key_label = tk.Label(self.frame, text="Key (single character):", font=("Arial", 20),bg="light pink")
        self.key_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.key_entry = tk.Entry(self.frame, font=("Arial", 20))
        self.key_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.value_label = tk.Label(self.frame, text="Value:", font=("Arial", 20), bg="light pink")
        self.value_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.value_entry = tk.Entry(self.frame, font=("Arial", 20))
        self.value_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Buttons for Insert, Search, Delete, and Traverse
        self.insert_button = tk.Button(self.frame, text="Insert", font=("Arial", 20), bg="light pink", command=self.insert)
        self.insert_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        self.search_button = tk.Button(self.frame, text="Search", font=("Arial", 20), bg="light pink", command=self.search)
        self.search_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
        self.delete_button = tk.Button(self.frame, text="Delete", font=("Arial", 20), bg="light pink", command=self.delete)
        self.delete_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
        self.traverse_button = tk.Button(self.frame, text="Traverse", font=("Arial", 20), bg="light pink", command=self.traverse)
        self.traverse_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        # Output Text for Results
        self.output_text = tk.Text(self.frame, height=10, width=50, font=("Arial", 20))
        self.output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def insert(self):
        key = self.key_entry.get()
        value = self.value_entry.get()
        if len(key) != 1 or not key.isalpha():
            self.output_text.insert(tk.END, "Error: Key must be a single alphabet character.\n")
            return
        if not value:
            self.output_text.insert(tk.END, "Error: Value cannot be empty.\n")
            return
        self.hash_table.insert(key, value)
        self.output_text.insert(tk.END, f"Inserted ('{key}', '{value}')\n")
        self.clear_entries()

    def search(self):
        key = self.key_entry.get()
        if len(key) != 1 or not key.isalpha():
            self.output_text.insert(tk.END, "Error: Key must be a single alphabet character.\n")
            return
        result = self.hash_table.search(key)
        if result:
            self.output_text.insert(tk.END, f"Search Result: Value for key '{key}': {result}\n")
        else:
            self.output_text.insert(tk.END, f"Search Result: Key '{key}' not found.\n")
        self.clear_entries()

    def delete(self):
        key = self.key_entry.get()
        if len(key) != 1 or not key.isalpha():
            self.output_text.insert(tk.END, "Error: Key must be a single alphabet character.\n")
            return
        success = self.hash_table.delete(key)
        if success:
            self.output_text.insert(tk.END, f"Deleted key '{key}'\n")
        else:
            self.output_text.insert(tk.END, f"Error: Key '{key}' not found.\n")
        self.clear_entries()

    def traverse(self):
        result = self.hash_table.traverse()
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        if result:
            for item in result:
                self.output_text.insert(tk.END, item + "\n")
        else:
            self.output_text.insert(tk.END, "Hash Table is empty.\n")

    def clear_entries(self):
        """Clear the key and value input fields after an operation."""
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)

# Hash Table with Collision Handling
class HashNode:
    def __init__(self, key, value):
        """Node for the linked list used in overflow chaining."""
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given key (based on ASCII value)."""
        return ord(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        new_node = HashNode(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def traverse(self):
        """Traverse and return all key-value pairs in the hash table."""
        result = []
        for index, node in enumerate(self.table):
            current = node
            chain = []
            while current:
                chain.append(f"[Key {current.key}, Value {current.value}]")
                current = current.next
            if chain:
                result.append(f"Index {index}: " + " -> ".join(chain))
        return result

# Main GUI class
def on_button_click(data_structure):
    if data_structure == "Stack":
        stack_window = tk.Toplevel(root)
        app = StackGUI(stack_window)
    elif data_structure == "Queue":
        queue_window = tk.Toplevel(root)
        app = QueueGUI(queue_window)
    elif data_structure == "Priority Queue":
        priority_queue_window = tk.Toplevel(root)
        app = PriorityQueueGUI(priority_queue_window)
    elif data_structure == "Linked List":
        linked_list_window = tk.Toplevel(root)
        app = LinkedListGUI(linked_list_window)
    elif data_structure == "Doubly Linked List":
        doubly_linked_list_window = tk.Toplevel(root)
        app = DoublyLinkedListGUI(doubly_linked_list_window)
    elif data_structure == "Graph":
        graph_window = tk.Toplevel(root)
        app = GraphGUI(graph_window)
    elif data_structure == "BFS":
        bfs_window = tk.Toplevel(root)
        app = BFSGUI(bfs_window)
    elif data_structure == "Binary Tree":
        binary_tree_window = tk.Toplevel(root)
        binary_tree = BinaryTree()
        app = BinaryTreeGUI(binary_tree)
    elif data_structure == "DFS":
        dfs_window = tk.Toplevel(root)
        app = DfSGUI(dfs_window)
    elif data_structure == "Huffman Tree":
        huffman_tree_window = tk.Toplevel(root)
        app = HuffmanApp(huffman_tree_window)
    elif data_structure == "Collision":
        hashtable_window = tk.Toplevel(root)
        app = CollisionGUI(hashtable_window)

# Create the main window
root = tk.Tk()
root.title("Data Structures")
root.state("zoomed")
root.configure(bg="light pink")

root.grid_rowconfigure((0,1,2,3,4), weight=1)
root.grid_columnconfigure((0,1,2,3,4), weight=1)

# Create a header label
header = tk.Label(root, text="   Jyoti Kumbhar S089 Data Structures   ", font=("Arial", 20), bg="light pink")
header.pack(pady=20)

# Function to create a section with a heading and buttons
def create_section(parent, items):
    section_frame = tk.Frame(parent, bg="light pink")
    section_frame.pack(pady=10)

    # Add buttons in a horizontal layout
    for col, item in enumerate(items):
        button = tk.Button(section_frame, text=item, font=("Arial", 20), bg="grey", fg="white",  command=lambda x=item: on_button_click(x))
        button.grid(row=1, column=col, padx=10, pady=5)

# Create frames for different sections
create_section(root, ["Stack", "Queue", "Priority Queue"])
create_section(root, ["Linked List", "Doubly Linked List","TSP"])
create_section(root, ["Binary Tree", "Huffman Tree","Graph"])
create_section(root, [ "BFS", "DFS"])
create_section(root, ["No Collision", "Collision"])

# Start the Tkinter event loop
root.mainloop()