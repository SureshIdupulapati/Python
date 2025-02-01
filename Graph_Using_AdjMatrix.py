class GraphMatrix:
    def __init__(self):
        """Initialize an empty adjacency matrix."""
        self.nodes = []  # List to store node names
        self.graph = []  # 2D list to store weights

    def add_node(self, v):
        """Add a new node to the graph and expand the adjacency matrix."""
        if v in self.nodes:
            print(f"Node '{v}' already exists.")
            return

        self.nodes.append(v)
        size = len(self.nodes)

        # Expand existing rows
        for row in self.graph:
            row.append(0)

        # Add a new row for the new node
        self.graph.append([0] * size)

    def add_edge(self, v1, v2, weight):
        """Add an undirected weighted edge between v1 and v2."""
        if v1 not in self.nodes or v2 not in self.nodes:
            missing = [v for v in (v1, v2) if v not in self.nodes]
            print(f"Error: Nodes {missing} are missing from the graph.")
            return

        index1, index2 = self.nodes.index(v1), self.nodes.index(v2)
        self.graph[index1][index2] = weight
        self.graph[index2][index1] = weight  # Ensure undirected property

    def remove_edge(self, v1, v2):
        """Remove an edge between v1 and v2."""
        if v1 not in self.nodes or v2 not in self.nodes:
            print(f"Error: One or both nodes are missing.")
            return

        index1, index2 = self.nodes.index(v1), self.nodes.index(v2)
        self.graph[index1][index2] = 0
        self.graph[index2][index1] = 0  # Remove from both sides

    def remove_node(self, v):
        """Remove a node and its edges from the graph."""
        if v not in self.nodes:
            print(f"Error: Node '{v}' does not exist.")
            return

        index = self.nodes.index(v)
        self.nodes.pop(index)
        self.graph.pop(index)  # Remove row

        for row in self.graph:
            row.pop(index)  # Remove corresponding column

    def display(self):
        """Display the adjacency matrix with labels."""
        if not self.nodes:
            print("Graph is empty.")
            return

        print("\nAdjacency Matrix:")
        print("  ", "  ".join(self.nodes))
        for i, row in enumerate(self.graph):
            print(f"{self.nodes[i]} {row}")


# Menu-driven interface
def menu():
    g = GraphMatrix()
    while True:
        print("\nGraph Operations:")
        print("1. Add Node")
        print("2. Add Edge")
        print("3. Remove Node")
        print("4. Remove Edge")
        print("5. Display Graph")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            node = input("Enter node name: ").strip()
            g.add_node(node)

        elif choice == '2':
            v1 = input("Enter first node: ").strip()
            v2 = input("Enter second node: ").strip()
            weight = int(input("Enter weight: "))
            g.add_edge(v1, v2, weight)

        elif choice == '3':
            node = input("Enter node name to remove: ").strip()
            g.remove_node(node)

        elif choice == '4':
            v1 = input("Enter first node: ").strip()
            v2 = input("Enter second node: ").strip()
            g.remove_edge(v1, v2)

        elif choice == '5':
            g.display()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Run the menu-driven program
menu()
