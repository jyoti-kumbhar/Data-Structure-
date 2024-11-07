class Node:
    def __init__(self, key, value):
        """Node for the linked list used in overflow chaining."""
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def size(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given key."""
        return key % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                print(current.value)
            current = current.next

        return None

    def traverse(self):
        """Traverse and print all key-value pairs in the hash table."""
        for index, node in enumerate(self.table):
            current = node
            while current:
                print(f"Index {index}: Key {current.key}, Value {current.value}")
                current = current.next

def operation():
    ht = HashTable()
    while True:
        print("----------------Hash Table----------------")
        print("S074 kermeen deboo")
        print(" 1.Size of Table\n 2.Insert into Table\n 3.Delete an Element\n 4.Search\n 5.Traverse\n 6.Exit")
        choice = int(input("Enter your choice(1-6): "))
        if choice == 1:
            size = int(input("Enter the size of array: "))
            ht.size(size)
        elif choice == 2:
            key=int(input("Enter the key: "))
            value=input("Enter the Value for the key: ")
            ht.insert(key, value)
        elif choice == 3:
            key=int(input("Enter the key: "))
            ht.delete(key)
        elif choice == 4:
            key=int(input("Enter the key: "))
            ht.search(key)
        elif choice == 5:
            ht.traverse()
        elif choice == 6:
            print("Exiting....")
            break
        else:
            print("Invalid choice.")
operation()
