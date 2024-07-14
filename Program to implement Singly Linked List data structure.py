class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        print(f"{deleted_node.data} is deleted from the beginning")
        return deleted_node.data
    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            print(f"{deleted_node.data} is deleted from the end")
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        print(f"{deleted_node.data} is deleted from the end")
        return deleted_node.data
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
class Operations:
    @staticmethod
    def linked_list_operation():
        linked_list = SingleLinkedList()
        while True:
            print("\nSingly Linked List\n1. Is empty\n2. Insert at beginning\n3. Insert at end\n4. Delete at beginning\n5. Delete at end\n6. Traverse\n7. Exit")
            choice = int(input("Enter your choice (1-7): "))
            if choice == 1:
                if linked_list.is_empty():
                    print("Linked List is empty")
                else:
                    print("Linked List is not empty")
            elif choice == 2:
                data = input("Enter the data: ")
                linked_list.insert_at_beginning(data)
            elif choice == 3:
                data = input("Enter the data: ")
                linked_list.insert_at_end(data)
            elif choice == 4:
                linked_list.delete_at_beginning()
            elif choice == 5:
                linked_list.delete_at_end()
            elif choice == 6:
                linked_list.traverse()
            elif choice == 7:
                print("Exiting")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
Operations.linked_list_operation()

