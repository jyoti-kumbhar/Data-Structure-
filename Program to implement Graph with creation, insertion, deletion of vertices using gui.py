import tkinter as tk
from tkinter import messagebox

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def get_adjacent(self, vertex):
        return self.graph.get(vertex, [])

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Operations")
        self.root.state("zoomed")
        self.root.configure(bg="#F08080")

        self.graph = Graph()

        # Canvas for Graph
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.grid(row=1, column=3, rowspan=6, padx=10, pady=10)

        self.name_label = tk.Label(root, text="Jyoti Kumbhar S089", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        # Add Vertex
        self.vertex_label = tk.Label(root, text="Vertex:", font=("Arial", 12))
        self.vertex_label.grid(row=1, column=0, padx=10, pady=10)
        self.vertex_entry = tk.Entry(root, font=("Arial", 12))
        self.vertex_entry.grid(row=1, column=1, padx=10, pady=10)
        self.add_vertex_button = tk.Button(root, text="Add Vertex", font=("Arial", 12), command=self.add_vertex)
        self.add_vertex_button.grid(row=1, column=2, padx=10, pady=10)

        # Remove Vertex
        self.remove_vertex_button = tk.Button(root, text="Remove Vertex", font=("Arial", 12), command=self.remove_vertex)
        self.remove_vertex_button.grid(row=2, column=2, padx=10, pady=10)

        # Add Edge
        self.vertex1_label = tk.Label(root, text="Vertex 1:", font=("Arial", 12))
        self.vertex1_label.grid(row=3, column=0, padx=10, pady=10)
        self.vertex1_entry = tk.Entry(root, font=("Arial", 12))
        self.vertex1_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.vertex2_label = tk.Label(root, text="Vertex 2:", font=("Arial", 12))
        self.vertex2_label.grid(row=4, column=0, padx=10, pady=10)
        self.vertex2_entry = tk.Entry(root, font=("Arial", 12))
        self.vertex2_entry.grid(row=4, column=1, padx=10, pady=10)
        
        self.add_edge_button = tk.Button(root, text="Add Edge", font=("Arial", 12), command=self.add_edge)
        self.add_edge_button.grid(row=5, column=1, padx=10, pady=10)
        
        self.remove_edge_button = tk.Button(root, text="Remove Edge", font=("Arial", 12), command=self.remove_edge)
        self.remove_edge_button.grid(row=5, column=2, padx=10, pady=10)

        # Display Graph
        self.display_button = tk.Button(root, text="Display Graph", font=("Arial", 12), command=self.display_graph)
        self.display_button.grid(row=5, column=0, pady=10)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a vertex.")

    def remove_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.remove_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a vertex.")

    def add_edge(self):
        vertex1 = self.vertex1_entry.get()
        vertex2 = self.vertex2_entry.get()
        if vertex1 and vertex2:
            self.graph.add_edge(vertex1, vertex2)
            self.vertex1_entry.delete(0, tk.END)
            self.vertex2_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both vertices.")

    def remove_edge(self):
        vertex1 = self.vertex1_entry.get()
        vertex2 = self.vertex2_entry.get()
        if vertex1 and vertex2:
            self.graph.remove_edge(vertex1, vertex2)
            self.vertex1_entry.delete(0, tk.END)
            self.vertex2_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both vertices.")

    def display_graph(self):
        self.canvas.delete("all")
        vertex_positions = {}
        level = 0
        y_spacing = 100
        x_spacing = 150

        def draw_vertex(vertex, x, y, level):
            if vertex in vertex_positions:
                return

            vertex_positions[vertex] = (x, y)
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="#F08080")
            self.canvas.create_text(x, y, text=vertex, font=("Arial", 14,))

            adjacent_vertices = self.graph.get_adjacent(vertex)
            next_y = y + y_spacing
            next_x = x - (len(adjacent_vertices) - 1) * x_spacing // 2
            for adj_vertex in adjacent_vertices:
                if adj_vertex not in vertex_positions:
                    self.canvas.create_line(x, y, next_x, next_y)
                    draw_vertex(adj_vertex, next_x, next_y, level+1)
                next_x += x_spacing

        # Start drawing from the first vertex in the graph
        if self.graph.graph:
            start_vertex = next(iter(self.graph.graph))
            draw_vertex(start_vertex, 400, 50, level)

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
