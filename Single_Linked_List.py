class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class S_LinkedList:
    def __init__(self):
        self.head = None

    def print_SLL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "-->", end=" ")
                temp = temp.ref
            print("None")

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref is not None:
                temp = temp.ref
            temp.ref = new_node

    def add_after_element(self, data, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                new_node = Node(data)
                new_node.ref = temp.ref
                temp.ref = new_node
                return
            temp = temp.ref
        print("Element not present in the Linked List!")

    def add_before_element(self, data, element):
        if self.head is None:
            print("Linked List is empty!")
        elif self.head.data == element:
            self.add_begin(data)
        else:
            temp = self.head
            while temp.ref is not None:
                if temp.ref.data == element:
                    new_node = Node(data)
                    new_node.ref = temp.ref
                    temp.ref = new_node
                    return
                temp = temp.ref
            print("Element not present in the Linked List!")

    def remove_begin(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            self.head = self.head.ref

    def remove_end(self):
        if self.head is None:
            print("Linked List is empty!")
        elif self.head.ref is None:
            self.head = None
        else:
            temp = self.head
            while temp.ref.ref is not None:
                temp = temp.ref
            temp.ref = None

    def remove_by_value(self, value):
        if self.head is None:
            print("Linked List is empty!")
        elif self.head.data == value:
            self.head = self.head.ref
        else:
            temp = self.head
            while temp.ref is not None:
                if temp.ref.data == value:
                    temp.ref = temp.ref.ref
                    return
                temp = temp.ref
            print("Element not present in the Linked List!")


SLL = S_LinkedList()
while True:
    print("\nChoose an operation:")
    print("1. Add at beginning")
    print("2. Add at end")
    print("3. Add after an element")
    print("4. Add before an element")
    print("5. Remove from beginning")
    print("6. Remove from end")
    print("7. Remove by value")
    print("8. Print Linked List")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        SLL.add_begin(data)
    elif choice == 2:
        data = int(input("Enter data: "))
        SLL.add_end(data)
    elif choice == 3:
        data = int(input("Enter data: "))
        element = int(input("Enter element after which to insert: "))
        SLL.add_after_element(data, element)
    elif choice == 4:
        data = int(input("Enter data: "))
        element = int(input("Enter element before which to insert: "))
        SLL.add_before_element(data, element)
    elif choice == 5:
        SLL.remove_begin()
    elif choice == 6:
        SLL.remove_end()
    elif choice == 7:
        value = int(input("Enter value to remove: "))
        SLL.remove_by_value(value)
    elif choice == 8:
        SLL.print_SLL()
    elif choice == 9:
        break
    else:
        print("Invalid choice, try again!")
