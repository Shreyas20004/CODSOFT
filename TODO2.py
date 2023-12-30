import tkinter
#All the elements of the window comes between the window and the main loop
# Create a window
root = tkinter.Tk()
# WidthXHeight
root.geometry("524x524")

#chane background Colour
root.configure(bg="White")

#Change the title
root.title("My To-Do List")

# Empty list
tasks = []
def update_lb():
    clear_lb()
    # populate task
    for task in tasks:
        lb_task.insert("end",task)

def clear_lb():
    lb_task.delete(0, "end")
def add_task():
    update_lb()
    global tasks
    tasks.append(txt_Entry.get())
    update_lb()

def Clear():
    global tasks
    tasks = []
    update_lb()

def Delete():
    lb_task.delete(0)

def SortAsc():
    tasks.sort()
    update_lb()

def Sort_dec():
    tasks.sort()
    tasks.reverse()
    update_lb()

def Tasks():
    no_tasks = len(tasks)
    msg = "No of tasks is %s"%no_tasks
    lbl_display["text"]=msg


lbl_title = tkinter.Label(root,text="To-do-list",bg="White")
lbl_title.pack()
lbl_display = tkinter.Label(root,text="",bg="White")
lbl_display.pack()
txt_Entry = tkinter.Entry(root,width=15)
txt_Entry.pack()
button_addTask = tkinter.Button(root, text="Add Task", fg="Green", bg="White",command=add_task)
button_addTask.pack()
button_clear = tkinter.Button(root, text="Clear", fg="Green", bg="White",command=Clear)
button_clear.pack()

button_delete1 = tkinter.Button(root, text="Delete first", fg="Green", bg="White",command=Delete)
button_delete1.pack()

button_sortAsc = tkinter.Button(root, text="Sort Ascending", fg="Green", bg="White",command=SortAsc)
button_sortAsc.pack()

button_sortDec = tkinter.Button(root, text="Sort Descending", fg="Green", bg="White",command=Sort_dec)
button_sortDec.pack()

button_Tasks = tkinter.Button(root, text="No of tasks", fg="Green", bg="White",command=Tasks)
button_Tasks.pack()

button_exit = tkinter.Button(root, text="Exit", fg="Green", bg="White",command=exit)
button_exit.pack()

lb_task = tkinter.Listbox(root)
lb_task.pack()







#Start the main  events in the loop
root.mainloop()