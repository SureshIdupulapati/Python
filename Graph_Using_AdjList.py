class GraphAdjList:
    def __init__(self):
        """Initialize an empty adjacency list."""
        self.graph_dict = {}

    def add_node(self, v):
        """Add a node to the graph."""
        if v in self.graph_dict:
            print(f"Node '{v}' already exists.")
        else:
            self.graph_dict[v] = []

    def add_edge(self, v1, v2, weight):
        """Add an undirected weighted edge between v1 and v2."""
        if v1 not in self.graph_dict or v2 not in self.graph_dict:
            print(f"Error: One or both nodes are missing.")
            return

        self.graph_dict[v1].append((v2, weight))
        self.graph_dict[v2].append((v1, weight))  # Ensure undirected property

    def remove_edge(self, v1, v2):
        """Remove an edge between v1 and v2."""
        if v1 not in self.graph_dict or v2 not in self.graph_dict:
            print(f"Error: One or both nodes are missing.")
            return

        self.graph_dict[v1] = [(v, w) for v, w in self.graph_dict[v1] if v != v2]
        self.graph_dict[v2] = [(v, w) for v, w in self.graph_dict[v2] if v != v1]

    def remove_node(self, v):
        """Remove a node and its edges from the graph."""
        if v not in self.graph_dict:
            print(f"Error: Node '{v}' does not exist.")
            return

        self.graph_dict.pop(v)  # Remove the node itself
        # Remove edges associated with this node
        for node in self.graph_dict:
            self.graph_dict[node] = [(v2, w) for v2, w in self.graph_dict[node] if v2 != v]

    def display(self):
        """Display the adjacency list."""
        if not self.graph_dict:
            print("Graph is empty.")
            return

        print("\nAdjacency List:")
        for node, edges in self.graph_dict.items():
            print(f"{node} -> {', '.join([f'({v}, {w})' for v, w in edges])}")

# Menu-driven interface
def menu():
    g = GraphAdjList()
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
