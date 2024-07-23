#Program to implement Priority Queue using a list and the heapq module for efficient operations
import heapq

class priorityQueue:
    def __init__(self):
        self.queue=[]
        self.size=int(input("Enter the size of queue: "))

    def isEmpty(self):
        return len(self.queue)==0
    
    def enqueue(self):
        if len(self.queue)>=self.size:
            print("Overflow. Cannot Enqueue item")
            return None
        item = input("Enter the item: ")
        priority = int(input(f"Enter the priority of {item}: "))
        heapq.heappush(self.queue,(priority, item))

    def dequeue(self):
        if self.isEmpty():
            print("Underflow. Cannot Dequeue")
            return None
        return heapq.heappop(self.queue)[1]
    
    def peek(self):
        if self.isEmpty():
            print("Underflow. Cannot Dequeue")
            return None
        return heapq.nsmallest(1, self.queue)[0][1]
    
    def traverse(self):
        if self.isEmpty():
            print("Underflow. Cannot Traverse.")
            return None
        print("Priority Queue element:")
        for i,j in self.queue:
            print(f"Priority: {i} Item: {j} ")
        print()

def operation():
    pq=priorityQueue()
    while True:
        print("----------------Priority Queue----------------")
        print("\n1.Is empty \n2.Enqueue \n3.Dequeue \n4.Peek \n5.Traverse \n6.Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            if pq.isEmpty():
                print("Queue is Empty")
            else:
                print("Queue is not Empty")

        elif choice==2:
            pq.enqueue()
        
        elif choice==3:
            print(f"Dequeued element: {pq.dequeue()}")

        elif choice==4:
            print(f"Peek element: {pq.peek()}")

        elif choice==5:
            pq.traverse()

        elif choice==6:
            print("Exiting")
            break

        else:
            print("Invalid choice. Enter the valid number.")

if __name__=="__main__":
    operation()