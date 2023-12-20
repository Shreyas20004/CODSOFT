todo = []

def Add_task():
    task = input("Enter the task:")
    todo.append(task)
    print("Task added!!")
    
def List_tasks():
    if len(todo) == 0:
        print("No tasks to display.")
    else:
        print("Printing tasks:")
        for i, task in enumerate(todo):
            print(f"{i+1}. {task}")

def List_delete():
    if len(todo) == 0:
        print("No tasks to delete.")
    else:
        print("printing values:")
        for i, task in enumerate(todo):
            print(f"{i+1} . {task}")
    sel = int(input("The index of task completed:"))
        
    if 0 <= int(sel) <= len(todo):
        del todo[sel-1]
        print("task completed")
    else:
        print("invalid task number")

def main():
    while True:
        print("\n\nMenu:\n1.Add Task \n2.List Tasks \n3.Delete Task \n4.Quit")
        ch=int(input("Enter your option:"))
        if ch==1:
            Add_task()
        if ch==2:
            List_tasks()
        elif ch==3:
            List_delete()
        elif ch==4:
            break
        
    print("Thanks")


if __name__=="__main__":
    main()