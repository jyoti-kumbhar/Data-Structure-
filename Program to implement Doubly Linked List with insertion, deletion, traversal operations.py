#Practical No.4
#AIM :Doubly Linked list with insertion, deletion, traversal operations

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_Node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_Node  # if empty = head, tail is at the same node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node

    def insert_at_end(self, data):
        new_Node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_Node  # if empty = head, tail is at the same node
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = new_Node

    def delete_at_beginning(self):
        if self.is_empty():
            print("List is empty.")
            return None
        deleted_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty.")
            return None
        deleted_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node.data

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end="<-->")
            current = current.next
        print("None")

class Operation:
    @staticmethod
    def doubly_linked_list():
        linked_list = DoublyLinkedList()
        while True:
            print("----------------DoublyLinkedList----------------")
            print("\nDoubly Linked List")
            print("1. is empty")
            print("2. insert at beginning")
            print("3. insert at end")
            print("4. delete at beginning")
            print("5. delete at end")
            print("6. display doubly linked list")
            print("7. exit")
            choice = int(input("Enter the choice (1-7): "))

            if choice == 1:
                if linked_list.is_empty():
                    print("Doubly Linked List is empty")
                else:
                    print("Doubly Linked List is not empty")

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

Operation.doubly_linked_list()
