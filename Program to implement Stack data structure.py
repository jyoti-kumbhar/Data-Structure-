#Practical No.2
#AIM: Stack with insertion, deletion, traversal operations

class Stack:
    def __init__(self):
        self.array = []
        self.size = int(input("Enter the Length of Stack:"))
        self.top = -1  # stack is empty

    def is_empty(self):
        return len(self.array) == 0        

    def push(self, element):
        # Check Overflow or Stack is Full
        if self.top >= self.size - 1:
            print("Stack Full.")
        else:
            self.top += 1
            self.array.append(element)
            print(f"{element} pushed to stack")


    def pop(self):
        # Check Underflow or Stack Empty
        if self.is_empty():
            print("Stack Empty.")
            return None
        else:
            element = self.array[self.top]
            self.array.remove(element)
            self.top -= 1
            return element

    def peek(self):
        if self.top == -1:
            return None
        else:
            return self.array[self.top]

    def display(self):
        print(self.array)

def stack_operations():
    stack = Stack()
    while True:
        print("\n Stack Operations \n 1.Push \n 2.Pop \n 3.Peek \n 4.Is Empty \n 5.Display \n 6.Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == '1':
            element = input("Enter the element: ")
            stack.push(element)

        elif choice == '2':
            try:
                element = stack.pop()
                print(f"{element} poped from stack")
            except IndexError as i:
                print(i)

        elif choice == '3':
            try:
                element = stack.peek()
                print(f"Top element in stack : {element} ")
            except IndexError as i:
                print(i)

        elif choice == '4':
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")

        elif choice == '5':
            stack.display()
            
        elif choice == '6':
            print("existing")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    stack_operations()

