# Smart to do app
# This app will help you to manage your tasks and to do list in a smart way.

print("Welcome to the Smart To Do App!")
print("Menu:\n1.Add a task\n2.View tasks\n3.Prioritize tasks\n4.Mark task as completed\n5.Edit a task\n6.Delete task\n7.Exit")

tasks = []  #tasks is an empty list it will store the tasks that the user will add to the app.

while True:    #while loop is used to keep the app runing untill the use chooses to exit the app.
    choice = input("Enter your choice 1-7: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)  #append is used to add the task to the list of tasks. It adds the task at the end of the list.
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks found!")
        else:
            print("Your tasks:")
            for num, task in enumerate(tasks, 1): #enumerate is used to get the index of the task. The index starts from 1.
                print(num, task)

    elif choice == "3":
        if not tasks:
            print("No tasks found!")
        else:
            print("Your tasks:")
            for num, task in enumerate(tasks, 1):  #for loop is used to print the tasks with their numbers.
                print(num, task)
            num = int(input("Enter the task number to prioritize: "))
            if 1 <= num <= len(tasks):
                updated = []
                updated.append(tasks[num - 1])  #-1 is used to get the task from the list of tasks. The index starts from 0, so we need to subtract 1 from the task number.
                for i, task in enumerate(tasks, 1):
                    if i != num:
                        updated.append(task)
                tasks = updated
                print("Task prioritized successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        if not tasks:
            print("No tasks found!")
        else:
            print("Your tasks:")
            for num, task in enumerate(tasks, 1):
                print(num, task)
            num = int(input("Enter the task number to mark as completed: "))
            if 1 <= num <= len(tasks):
                updated = [] #updated is a new list that will store the tasks after marking that task as completed.
                for i, task in enumerate(tasks, 1):
                    if i != num:  
                        updated.append(task)
                tasks = updated
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    elif choice == "5":
        if not tasks:
            print("No tasks found!")
        else:
            print("Your tasks:")
            for num, task in enumerate(tasks, 1):
                print(num, task)
            num = int(input("Enter the task number to edit: "))
            if 1 <= num <= len(tasks):  #Len is used to  know the length of the list of tasks.
                value = input("Enter the new task: ")
                tasks[num - 1] = value
                print("Task edited successfully!")
            else:
                print("Invalid task number!")

    elif choice == "6":
        if not tasks:
            print("No tasks found!")
        else:
            print("Your tasks:")
            for num, task in enumerate(tasks, 1):
                print(num, task)
            num = int(input("Enter the task number to delete: "))
            if 1 <= num <= len(tasks):  #<= is used to check if the task number is valid or not. It is valid if the task number is between 1 and the length of the list of tasks.
                updated = []
                for i, task in enumerate(tasks, 1):
                    if i != num:
                        updated.append(task)  #updated is a new list that will store the tasks after deleting that task which the user wants to delete.
                tasks = updated
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == "7":
        print("Thank you for using the Smart To Do App! Goodbye!")
        break   #break is used to exit the while loop when the user chooses to exit the app.

    else:
        print("Invalid choice! Please enter a number between 1-7.")