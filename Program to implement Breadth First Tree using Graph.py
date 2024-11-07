import matplotlib.pyplot as plt
import networkx as nx
from collections import deque, defaultdict

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

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

    def visualize(self, bfs_tree=None):
        G = nx.Graph(self.graph)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(12, 6))

        # Draw the BFS Tree
        if bfs_tree:
            # Create a graph from the BFS Tree
            T = nx.DiGraph(bfs_tree)
            pos_tree = nx.spring_layout(T)
            nx.draw(T, pos_tree, with_labels=True, node_color='lightblue', edge_color='black', node_size=1000, font_size=15, font_weight='bold', arrows=True)
            plt.title("BFS Tree")

        plt.show()

def print_bfs_tree(bfs_tree, start):
    """Print the Breadth-First Tree."""
    print(f"Breadth-First Tree starting from {start}:")
    for vertex in bfs_tree:
        print(f"{vertex}: {bfs_tree[vertex]}")

def main():
    print("S089 Jyoti Kumbhar")
    g = Graph()

    while True:
        print("--------------Graph Operations--------------")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Display the Graph")
        print("4. Print BFS Tree")
        print("5. Visualize the Graph")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            num_vertices = int(input("Enter the number of vertices: "))
            for _ in range(num_vertices):
                vertex = input("Enter vertex: ")
                g.add_vertex(vertex)

        elif choice == 2:
            num_edges = int(input("Enter the number of edges: "))
            for _ in range(num_edges):
                vertex1 = input("Enter the first vertex of the edge: ")
                vertex2 = input("Enter the second vertex of the edge: ")
                g.add_edge(vertex1, vertex2)

        elif choice == 3:
            print("Graph: ")
            g.display()
        
        elif choice == 4:
            start_vertex = input("Enter the starting point: ")
            bfs_tree = g.bfs_tree(start_vertex)
            print_bfs_tree(bfs_tree, start_vertex)
            
        elif choice == 5:
                start_vertex = input("Enter the starting point: ")
                bfs_tree = g.bfs_tree(start_vertex)
                g.visualize(bfs_tree)

        elif choice == 6:
            print("Exiting.....")
            break
        
        else:
            print("Invalid choice. Enter a valid choice (1-6)")

if __name__ == "__main__":
    main()
