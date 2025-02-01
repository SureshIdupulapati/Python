class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insertion(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key is None:
            print("Tree is empty!")
            return
        if self.key == data:
            print(f"Element {data} Found in the tree.")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f"Element {data} not present in the tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f"Element {data} not present in the tree!")

    def pre_order_BST(self):
        if self.key is None:
            print("Tree is empty!")
        else:
            print(self.key, end=" ")
            if self.lchild:
                self.lchild.pre_order_BST()
            if self.rchild:
                self.rchild.pre_order_BST()

    def in_order_BST(self):
        if self.key is None:
            print("Tree is empty!")
        else:
            if self.lchild:
                self.lchild.in_order_BST()
            print(self.key, end=" ")
            if self.rchild:
                self.rchild.in_order_BST()

    def post_order_BST(self):
        if self.key is None:
            print("Tree is empty!")
        else:
            if self.lchild:
                self.lchild.post_order_BST()
            if self.rchild:
                self.rchild.post_order_BST()
            print(self.key, end=" ")

    def find_minimum(self):
        current = self
        while current.lchild:
            current = current.lchild
        return current

    def deletion(self, data):
        if self.key is None:
            print("Tree is empty!")
            return None

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print(f"Element {data} not present in the tree!")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print(f"Element {data} not present in the tree!")
        else:
            # Case 1: Node is a leaf
            if self.lchild is None and self.rchild is None:
                return None  # Remove the node

            # Case 2: Node has one child
            if self.lchild is None:
                return self.rchild  # Replace with right child
            if self.rchild is None:
                return self.lchild  # Replace with left child

            # Case 3: Node has two children
            min_node = self.rchild.find_minimum()
            self.key = min_node.key
            self.rchild = self.rchild.deletion(min_node.key)

        return self

    def min_element(self):
        if self.key is None:
            print("Tree is empty!")
        else:
            temp = self
            while temp.lchild:
                temp = temp.lchild
            print("Minimum Element:", temp.key)

    def max_element(self):
        if self.key is None:
            print("Tree is empty!")
        else:
            temp = self
            while temp.rchild:
                temp = temp.rchild
            print("Maximum Element:", temp.key)


# Menu-Driven Program
def menu():
    bst = None  # Initially, the tree is empty

    while True:
        print("\n===== Binary Search Tree Operations =====")
        print("1. Insert an Element")
        print("2. Search for an Element")
        print("3. Delete an Element")
        print("4. Pre-Order Traversal")
        print("5. In-Order Traversal")
        print("6. Post-Order Traversal")
        print("7. Find Minimum Element")
        print("8. Find Maximum Element")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            data = int(input("Enter the value to insert: "))
            if bst is None:
                bst = BST(data)
            else:
                bst.insertion(data)
            print(f"Inserted {data} into the tree.")

        elif choice == "2":
            if bst is None:
                print("Tree is empty!")
            else:
                data = int(input("Enter the value to search: "))
                bst.search(data)

        elif choice == "3":
            if bst is None:
                print("Tree is empty!")
            else:
                data = int(input("Enter the value to delete: "))
                bst = bst.deletion(data)
                print(f"Deleted {data} from the tree.")

        elif choice == "4":
            if bst is None:
                print("Tree is empty!")
            else:
                print("Pre-Order Traversal: ", end="")
                bst.pre_order_BST()
                print()

        elif choice == "5":
            if bst is None:
                print("Tree is empty!")
            else:
                print("In-Order Traversal: ", end="")
                bst.in_order_BST()
                print()

        elif choice == "6":
            if bst is None:
                print("Tree is empty!")
            else:
                print("Post-Order Traversal: ", end="")
                bst.post_order_BST()
                print()

        elif choice == "7":
            if bst is None:
                print("Tree is empty!")
            else:
                bst.min_element()

        elif choice == "8":
            if bst is None:
                print("Tree is empty!")
            else:
                bst.max_element()

        elif choice == "9":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 9.")


# Run the menu
menu()
