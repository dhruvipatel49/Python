queue = []

while True:
    print("1. Enqueue\n2. Dequeue\n3. Peek\n4. Display\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter the element to enqueue: "))
        queue.append(element)
    elif choice == 2:
        if queue:
            print("Dequeued element:", queue.pop(0))
        else:
            print("Queue is empty")
    elif choice == 3:
        if queue:
            print("Front element:", queue[0])
        else:
            print("Queue is empty")
    elif choice == 4:
        print("Queue contents:", queue)
    elif choice == 5:
        break
    else:
        print("Invalid choice")