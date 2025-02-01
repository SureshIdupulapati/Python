class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class D_LinkedList:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "-->", end=" ")
                temp = temp.nref
            print("NULL")

    def print_DLL_reverse(self):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            temp = self.head
            while temp.nref is not None:
                temp = temp.nref
            while temp is not None:
                print(temp.data, "-->", end=" ")
                temp = temp.pref
            print("NULL")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.nref is not None:
                temp = temp.nref
            new_node.pref = temp
            temp.nref = new_node

    def add_after_element(self, data, element):
        temp = self.head
        while temp is not None:
            if temp.data == element:
                new_node = Node(data)
                new_node.pref = temp
                new_node.nref = temp.nref
                if temp.nref is not None:
                    temp.nref.pref = new_node
                temp.nref = new_node
                return
            temp = temp.nref
        print("Element not found!")

    def add_before_element(self, data, element):
        if self.head is None:
            print("LinkedList is empty!")
            return
        if self.head.data == element:
            self.add_begin(data)
            return
        temp = self.head
        while temp is not None:
            if temp.data == element:
                new_node = Node(data)
                new_node.nref = temp
                new_node.pref = temp.pref
                if temp.pref is not None:
                    temp.pref.nref = new_node
                temp.pref = new_node
                return
            temp = temp.nref
        print("Element not found!")

    def remove_begin(self):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            self.head = self.head.nref
            if self.head is not None:
                self.head.pref = None

    def remove_end(self):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            temp = self.head
            while temp.nref is not None:
                temp = temp.nref
            if temp.pref is not None:
                temp.pref.nref = None
            else:
                self.head = None

    def remove_by_value(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                if temp.pref is None:
                    self.head = temp.nref
                    if self.head is not None:
                        self.head.pref = None
                elif temp.nref is None:
                    temp.pref.nref = None
                else:
                    temp.pref.nref = temp.nref
                    temp.nref.pref = temp.pref
                return
            temp = temp.nref
        print("Element not found!")


DLL = D_LinkedList()

while True:
    print("\nOperations: ")
    print("1. Add at beginning")
    print("2. Add at end")
    print("3. Add after an element")
    print("4. Add before an element")
    print("5. Remove from beginning")
    print("6. Remove from end")
    print("7. Remove by value")
    print("8. Print Linked List")
    print("9. Print Linked List in Reverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter value: "))
        DLL.add_begin(data)
    elif choice == 2:
        data = int(input("Enter value: "))
        DLL.add_end(data)
    elif choice == 3:
        data = int(input("Enter value: "))
        element = int(input("Enter element after which to insert: "))
        DLL.add_after_element(data, element)
    elif choice == 4:
        data = int(input("Enter value: "))
        element = int(input("Enter element before which to insert: "))
        DLL.add_before_element(data, element)
    elif choice == 5:
        DLL.remove_begin()
    elif choice == 6:
        DLL.remove_end()
    elif choice == 7:
        value = int(input("Enter value to remove: "))
        DLL.remove_by_value(value)
    elif choice == 8:
        DLL.print_DLL()
    elif choice == 9:
        DLL.print_DLL_reverse()
    elif choice == 10:
        break
    else:
        print("Invalid choice! Try again.")
