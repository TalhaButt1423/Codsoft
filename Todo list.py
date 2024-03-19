#Program for TO-DO LIST
tasks=[]
print("\t*TO-DO LIST*")
print("\t<---------->")
#Function to add task
def addtask(Task):

    tasks.append(Task)
    return "New task added successfully"
#Function to remove task
def removeTask(num):
    num=int(num)
    num=num-1
    tasks.pop(num)
    return
#Function to view task
def viewTasks():
    print("----<YOUR TASKS>----")
    for x, task in enumerate(tasks, start=1):
        print(f"{x}.", task)
#MAIN Program
while True:

    print("1. Add a task")
    print("2. View all tasks")
    print("3. Edit a task")
    print("4. Remove a task")
    print("5. Delete all tasks")

    i = input("Enter your choice: ")
    print()
    #Code to add a Task
    if i == "1":
        while i!="0":
            n=input("Enter the task: ")
            if n!="":
                addtask(n)
                i = input("Are you done (0 to exit)?")
            else:
                print("Enter some task to save!")
    #Code to view task
    elif i == "2":
        viewTasks()
    #Code to edit task
    elif i=="3":
        viewTasks()
        j=int(input("Enter index number of task to be edited: "))
        j=j-1
        length=len(tasks)
        if j<=length and j>0:
            tasks[j]=input("Enter the edited task: ")
            print("Task successfully edited")
        else:
            print("Enter the correct Index number !")
    #Code to remove task
    elif i=="4":
        viewTasks()
        k=int(input("Enter the index number of task you wanna remove !"))
        lenh=len(tasks)
        if k<=lenh and k>0:
            removeTask(k)
            print("Task deleted successfully !")
        else:
            print("Enter the correct Index number !")
    #Code to delete all tasks
    elif i=="5":
        y=input("Are you sure to delete all the stored tasks!\nEnter '0' to confirm: ")
        if y=="0":
            tasks.clear()
            print("All tasks deleted successfully!")
        else:
            print("No task is deleted!")
            print()


    else:
        print("Enter the correct choice from above!")
    print()

