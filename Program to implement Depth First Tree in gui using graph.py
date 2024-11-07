import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import messagebox
from collections import defaultdict

class Graph:
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

        def dfs(v):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_tree[v].append(neighbor)
                    dfs(neighbor)

        dfs(start)
        return dfs_tree

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def original_graph(self):
        G = nx.Graph(self.graph)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(12, 6))

        # Draw the original graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=1000, font_size=14)
        plt.title("Graph")

        plt.show()

    def visualize(self, dfs_tree=None):
        """Visualize the graph and optionally the DFS tree."""
        plt.figure(figsize=(12, 6))

        # Draw the DFS Tree
        if dfs_tree:
            # Create a graph from the DFS Tree
            T = nx.DiGraph(dfs_tree)
            pos_tree = nx.spring_layout(T)
            nx.draw(T, pos_tree, with_labels=True, node_color='lightblue', edge_color='black', node_size=1000, font_size=14, arrows=True)
            plt.title("DFS Tree")

        plt.show()

# Create the GUI
class GraphApp:
    def __init__(self, root):
        self.graph = Graph()
        self.root = root
        self.root.title("Graph DFS Visualization")
        self.root.state("zoomed")
        self.root.configure(bg="lightcoral")
        bgcolor = "lightcoral"
        font="arial"
        fsize=14

        # Configure the grid layout for the entire window
        self.root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)


        self.name_label = tk.Label(root, text="Jyoti kumbhar S089", font=(font,fsize), bg=bgcolor)
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_label = tk.Label(root, text="DSF Graph", font=(font,fsize), bg=bgcolor)
        self.name_label.grid(row=0, column=1, padx=10, pady=10)

        # Create UI elements
        self.vertex_label = tk.Label(root, text="Vertex:", font=(font,fsize), bg=bgcolor)
        self.vertex_label.grid(row=1, column=0, padx=10, pady=10)
        self.vertex_entry = tk.Entry(root)
        self.vertex_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_vertex_button = tk.Button(root, text="Add Vertex", command=self.add_vertex, font=(font, fsize))
        self.add_vertex_button.grid(row=1, column=2, padx=10, pady=10)

        self.edge_label1 = tk.Label(root, text="Edge (V1):", font=(font,fsize), bg=bgcolor)
        self.edge_label1.grid(row=1, column=3, padx=10, pady=10)
        self.edge_entry1 = tk.Entry(root)
        self.edge_entry1.grid(row=1, column=4, padx=10, pady=10)

        self.edge_label2 = tk.Label(root, text="Edge (V2):", font=(font,fsize), bg=bgcolor)
        self.edge_label2.grid(row=3, column=3, padx=10, pady=10)
        self.edge_entry2 = tk.Entry(root)
        self.edge_entry2.grid(row=3, column=4, padx=10, pady=10)

        self.add_edge_button = tk.Button(root, text="Add Edge", command=self.add_edge, font=(font, fsize))
        self.add_edge_button.grid(row=3, column=5, padx=10, pady=10)

        self.start_vertex_label = tk.Label(root, text="Start Vertex for DFS:", font=(font,fsize), bg=bgcolor)
        self.start_vertex_label.grid(row=3, column=0, padx=10, pady=10)
        self.start_vertex_entry = tk.Entry(root)
        self.start_vertex_entry.grid(row=3, column=1, padx=10, pady=10)

        self.show_bfs_button = tk.Button(root, text="Show DFS Tree", command=self.show_dfs_tree, font=(font, fsize))
        self.show_bfs_button.grid(row=3, column=2, padx=10, pady=10)

        self.display_graph_button = tk.Button(root, text="Display Graph", command=self.display_graph, font=(font, fsize))
        self.display_graph_button.grid(row=4, column=1, padx=10, pady=10)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertex_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a vertex.")

    def add_edge(self):
        v1 = self.edge_entry1.get()
        v2 = self.edge_entry2.get()
        if v1 and v2:
            if v1 in self.graph.graph and v2 in self.graph.graph:
                self.graph.add_edge(v1, v2)
                self.edge_entry1.delete(0, tk.END)
                self.edge_entry2.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Both vertices must exist in the graph.")
        else:
            messagebox.showwarning("Input Error", "Please enter both vertices.")

    def show_dfs_tree(self):
        start = self.start_vertex_entry.get()
        if start:
            if start in self.graph.graph:
                dfs_tree = self.graph.dfs_tree(start)
                self.graph.visualize(dfs_tree)
            else:
                messagebox.showwarning("Input Error", "Start vertex must exist in the graph.")
        else:
            messagebox.showwarning("Input Error", "Please enter the start vertex.")

    def display_graph(self):
        self.graph.original_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
