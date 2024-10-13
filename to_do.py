def task():
    tasks = []
    print("Welcome To The Task Management System")
    
    total_tasks = int(input("Enter How many tasks do you want to add = "))
    for i in range(1, total_tasks+1):
        task_name =input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print(f"Today's tasks are\n{tasks}")