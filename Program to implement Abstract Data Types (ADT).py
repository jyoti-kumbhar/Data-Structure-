#Practical No.1
#AIM: Write a program to implement Abstract Data Types (ADT)

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0


# Function to interact with the queue using user input
def queue_operations():
    queue = Queue()
    while True:
        print("\nQueue Operations: \n1. Enqueue \n2. Dequeue \n3. Peek \n4. Size \n5. Is Empty \n6. Exit")
        
        choice = input("Enter your choice (1-6): ")

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
            try:
                element = queue.peek()
                print(f"Front element: {element}")
            except IndexError as e:
                print(e)

        elif choice == '4':
            print(f"Size of queue: {queue.size()}")

        elif choice == '5':
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Main function to run the program
if __name__ == "__main__":
    queue_operations()
