queue = []

while True:
    print("\nQueue Operations:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter element to enqueue: ")
        queue.append(item)
        print(f"{item} enqueued")
    elif choice == '2':
        if queue:
            print(f"Dequeued element: {queue.pop(0)}")
        else:
            print("Queue is empty!")
    elif choice == '3':
        print("Queue contents:", queue)
    elif choice == '4':
        break
    else:
        print("Invalid choice!")