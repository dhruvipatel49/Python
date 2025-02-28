stack = []

while True:
    print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter the element to push: "))
        stack.append(element)
    elif choice == 2:
        if stack:
            print("Popped element:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == 3:
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty")
    elif choice == 4:
        print("Stack contents:", stack)
    elif choice == 5:
        break
    else:
        print("Invalid choice")