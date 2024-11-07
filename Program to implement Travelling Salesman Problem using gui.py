import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TSPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solver")
        self.root.state('zoomed')
        self.root.configure(bg='lightblue')

        # Configure grid layout
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.root.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        tk.Label(root, text="Jyoti Kumbhar S089",font=('arial',14), bg='lightblue').grid(row=0, column=1, sticky='w')
        tk.Label(root, text="Travelling Salesman Problem",font=('arial',14), bg='lightblue').grid(row=0, column=2, sticky='w')

        # Input for list of places (forts)
        tk.Label(root, text="Places (comma-separated):",font=('arial',14), bg='lightblue').grid(row=1, column=1, sticky='w')
        self.forts_entry = tk.Entry(root, width=50, font=('arial',14))
        self.forts_entry.grid(row=1, column=2, columnspan=3)

        # Input for distance matrix
        tk.Label(root, text="Distance matrix (comma-separated values, rows separated by semicolons):",font=('arial',14), bg='lightblue').grid(row=2, column=1, sticky='w')
        self.matrix_entry = tk.Entry(root, width=50, font=('arial',14))
        self.matrix_entry.grid(row=2, column=2, columnspan=3)

        # Solve button
        self.solve_button = tk.Button(root, text="Solve TSP", command=self.solve_tsp, font=('arial',14), bg='lightblue')
        self.solve_button.grid(row=3, column=2, columnspan=2, )

        # Placeholder for result label
        self.result_label = tk.Label(root, text="",font=('arial',14), bg='lightblue')
        self.result_label.grid(row=4, column=1, columnspan=4, sticky='w')

    def solve_tsp(self):
        # Get forts input
        forts = self.forts_entry.get().split(',')
        forts = [fort.strip() for fort in forts if fort.strip()]
        num_forts = len(forts)

        # Get distance matrix input
        matrix_input = self.matrix_entry.get()
        try:
            # Convert the input into a 2D list (matrix)
            distance_matrix = [
                [int(x) for x in row.split(',')]
                for row in matrix_input.split(';')
            ]
            # Check if the matrix is valid (square matrix)
            if len(distance_matrix) != num_forts or any(len(row) != num_forts for row in distance_matrix):
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid matrix where rows are separated by semicolons and values are separated by commas.")
            return

        # Solve TSP
        tsp = TSP(distance_matrix, forts)
        best_route, min_distance = tsp.solve()

        # Display result
        route_str = " -> ".join([forts[i] for i in best_route])
        self.result_label.config(text=f"Optimal Route: {route_str}\nTotal Distance: {min_distance}")

        # Visualize the route in a new window
        self.visualize_graph(best_route, distance_matrix, forts, min_distance)

    def visualize_graph(self, route, distance_matrix, forts, min_distance):
        """Visualize the TSP route using matplotlib and networkx in a new window."""
        graph_window = tk.Toplevel(self.root)
        graph_window.title("TSP Route Visualization")

        figure = plt.Figure(figsize=(5, 5), dpi=100)
        canvas = FigureCanvasTkAgg(figure, graph_window)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        ax = figure.add_subplot(111)
        G = nx.Graph()

        # Add nodes (forts)
        for i, fort in enumerate(forts):
            G.add_node(i, label=fort)

        # Add edges based on the route
        for i in range(len(route) - 1):
            G.add_edge(route[i], route[i + 1], weight=distance_matrix[route[i]][route[i + 1]])

        # Add the edge from the last node back to the first to complete the loop
        G.add_edge(route[-1], route[0], weight=distance_matrix[route[-1]][route[0]])

        # Get node positions in a circular layout
        pos = nx.circular_layout(G)

        # Draw nodes and edges
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color='gray', ax=ax)

        # Label edges with distances
        edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

        # Label the forts
        nx.draw_networkx_labels(G, pos, labels={i: fort for i, fort in enumerate(forts)}, font_size=12, ax=ax)

        # Show total distance in the plot title
        ax.set_title(f"Optimal TSP Route (Total Distance: {min_distance})")
        ax.axis('off')
        canvas.draw()

class TSP:
    def __init__(self, distance_matrix, forts):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.forts = forts

    def calculate_total_distance(self, route):
        """Calculate the total distance of a given route."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        # Add distance to return to the starting city
        total_distance += self.distance_matrix[route[-1]][route[0]]
        return total_distance

    def solve(self):
        """Solve the TSP using brute force."""
        min_distance = math.inf
        best_route = None
        # Generate all possible permutations of cities (excluding the starting city)
        for perm in permutations(range(self.num_cities)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return best_route, min_distance

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPGUI(root)
    root.mainloop()
