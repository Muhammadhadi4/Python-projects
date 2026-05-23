#tasks managing
tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("Choose: ")
  if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("Task add ho gaya! ")
    
    elif choice == "2":
        for task in tasks:
            print(task)
    
    elif choice == "3":
        break
