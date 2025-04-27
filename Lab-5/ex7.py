stack = []

while True:
    print("\nStack Operations:\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter element to push: ")
        stack.append(item)
        print(f"{item} pushed to stack")
    elif choice == '2':
        if stack:
            print(f"Popped element: {stack.pop()}")
        else:
            print("Stack is empty!")
    elif choice == '3':
        print("Stack contents:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid choice!")