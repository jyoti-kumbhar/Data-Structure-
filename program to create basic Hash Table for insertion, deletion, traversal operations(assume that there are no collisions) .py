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
        self.table[index] = (key, value)
    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None
    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            print( self.table[index][1])
        return None
    def traverse(self):
        """Traverse and print all key-value pairs in the hash table."""
        for index, item in enumerate(self.table):
            if item is not None:
                key, value = item
                print(f"Index {index}: Key {key}, Value {value}")
def operation():
    ht = HashTable()
    while True:
        print("----------------Hash Table----------------")
        print("S074 Kermeen Deboo")
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
