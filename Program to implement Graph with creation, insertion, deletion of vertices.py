class Graph:
    def __init__(self):
        # empty dictionary
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        # removing edges
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            # removing vertex
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

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Function to take user input and populate the graph
def main():
    print("S089 Jyoti Kumbhar")
    g = Graph()

    while True:
        print("--------------Graph Operations--------------")
        print("1. Add Vertex")
        print("2. Remove Vertex")
        print("3. Add Edge")
        print("4. Remove Edge")
        print("5. Display the Graph")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            num_vertices = int(input("Enter the number of vertices: "))
            for _ in range(num_vertices):
                vertex = input("Enter vertex: ")
                g.add_vertex(vertex)

        elif choice == 2:
            vertex = input("Enter vertex: ")
            g.remove_vertex(vertex)

        elif choice == 3:
            num_edges = int(input("Enter the number of edges: "))
            for _ in range(num_edges):
                vertex1 = input("Enter the first vertex of the edge: ")
                vertex2 = input("Enter the second vertex of the edge: ")
                g.add_edge(vertex1, vertex2)

        elif choice == 4:
            vertex1 = input("Enter the first vertex of the edge to remove: ")
            vertex2 = input("Enter the second vertex of the edge to remove: ")
            g.remove_edge(vertex1, vertex2)

        elif choice == 5:
            print("Graph: ")
            g.display()
        
        elif choice == 6:
            print("Exiting.....")
            break
        
        else:
            print("Invalid choice. Enter a valid choice (1-6)")

if __name__ == "__main__":
    main()
