#Practical No.5
#AIM: Write a Program to implement Queue with insertion, deletion, traversal operations

class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    
    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
        
    def traverse(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", ' -> '.join(self.elements))


def queue_operations():
    queue = Queue()
    while True:
        print("\nQueue Operations: \n1. Enqueue \n2. Dequeue \n3. Traverse \n4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            element = input("Enter element to enqueue: ")
            queue.enqueue(element)
            print(f"{element} enqueued to queue.")

        elif choice == '2':
            try:
                element = queue.dequeue()
                print(f"{element} dequeued from queue.")
            except IndexError as e:
                print(e)

        elif choice == '3':
            queue.traverse()
        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Main function to run the program
if __name__ == "__main__":
    queue_operations()
