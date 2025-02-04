#To-Do List task
#Adding task
#Deleting task
#Marking as completed
#Show the list of tasks
#Exit

class ToDoList:
    def __init__(self):
        self.to_do_list = {}


    def add_task(self,task,status="Pending"):
        if task in self.to_do_list:
            print("The task is already added! Add new one!")
        else:
            self.to_do_list[task]= status
            print("\nTask Added Successfully!")

    def remove_task(self,task,status= "Pending"):
        if task in self.to_do_list:
            del self.to_do_list[task]
            print("\nTask is removed Successfully!")
        else:
            print("\nThe task doesn't exist in To-Do List")

    def mark_done(self,task,status = "Completed"):
        if task in self.to_do_list:
            self.to_do_list[task] = status
            print("Given task marked as done")
        else:
            print("\nThe task doesn't exist in To-Do List")

    def show_tasks(self):
        if self.to_do_list:
            print("\n Tasks              Status")
            print("-"*30)
            i = 1
            for task,status in self.to_do_list.items():
                print(f"\n{i}. {task}  - {status}")
                i+= 1
        else:
            print("Your To-Do List is Empty!")


obj = ToDoList()

while True:
    print("\nTo-Do List Menu:")
    print("1.Add a task")
    print("2.Remove a task")
    print("3.Mark a task as done")
    print("4.Display all tasks")
    print("5.Exit")

    choice = input("\nEnter your choice(1-5): ").strip()

    if choice == '1':
        task = input("Enter the task to add: ").capitalize().strip()
        obj.add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ").capitalize().strip()
        obj.remove_task(task)
    elif choice == '3':
        task = input("Enter the task to mark as done: ").capitalize().strip()
        obj.mark_done(task)
    elif choice == '4':
        obj.show_tasks()
    elif choice == '5':
        print("\nExiting the program...")
        print("\nThank you!\n")
        break
    else:
        print("Enter a valid choice in digits 1-5 only!")