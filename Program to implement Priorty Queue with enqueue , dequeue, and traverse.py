class priorityQueue:
    def __init__(self):
        self.queue=[]
        self.size = int(input("Enter the size of queue: "))

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, process, priority):  
        if  len(self.queue) >= self.size :
            print("Priority Queue is full")  #overflow
        else:
            self.queue.append((process, priority))
            self.queue.sort(key=lambda x:x[1])
            print(f"Enqueued: {process} with priority {priority}")
    
    def dequeue(self):
        if self.is_empty():
            print("Priority Queue is empty")   #underflow
        else:
            process=self.queue.pop(0)[0]
            print(f"Dequeued: {process}")

    def traverse(self):
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            print("Priority Queue contains:")
            for process, priority in self.queue:
                print(f"Process: {process}, Priority: {priority}")


# Function to interact with the queue using user input
def queue_operations():
    pqueue = priorityQueue()
    while True:
        print("--------------Priority Queue--------------")
        print("\n Priority Queue Operations: \n1. Is Empty \n2. Enqueue \n3. Dequeue \n4. Traverse \n5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if pqueue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")

        elif choice == '2':
            process = input("Enter the process: ")
            priority = int(input("Enter the priority of process: "))
            pqueue.enqueue(process, priority)

        elif choice == '3':
            pqueue.dequeue()

        elif choice == '4':
            pqueue.traverse()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Main function to run the program
if __name__ == "__main__":
    queue_operations()