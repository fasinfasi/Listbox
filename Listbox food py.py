
from tkinter import *
from tkinter import messagebox

def submit():
    items = []
    if not listbox.curselection(): #Nothing select whlie submit
        messagebox.showerror(title="Error", message="You have not select anyone")
    else:       
        for food in listbox.curselection():
            items.insert(food,listbox.get(food)) #insert selected food to list items
    
        print("You have ordered : ")
        for i in items:
            print(i)

def add():
    if not entry.get(): #Nothing select whlie adding
        messagebox.showerror(title="Error", message="You not input anything to add")
    
    else:
        print("You added : ",entry.get())
        listbox.insert(listbox.size(),entry.get()) #Add input foods into Listbox
        listbox.config(height=listbox.size()) #Adjust size of listbox
        
def deletebutton():
    delete_item = []
    
    if not listbox.curselection():
        messagebox.showerror(title="Error", message="You have not select anyone to delete")    
    
    else:
        for index in reversed(listbox.curselection()):
            delete_item.insert(index,listbox.get(index)) #Insert selected foods items to list delete_item
            listbox.delete(index) #Delete selected foods
        listbox.config(height=listbox.size()) #Adjust size of listbox
            
        print("Deleted item: ")
        for d in delete_item:
            print(d)

window = Tk()
window.title("Food Listbox")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("constantia",15),
                  selectmode=MULTIPLE
                  )
listbox.pack()
listbox.insert(1,"Pizza")
listbox.insert(2,"Hotdog")
listbox.insert(3,"sandwich")
listbox.insert(4,"Hamburger")
listbox.insert(5,"Donut")

listbox.config(height=listbox.size())

entry = Entry(window)
entry.config(fg="red")
entry.pack()

submit = Button(window,text="Submit",command=submit)
submit.pack()

add = Button(window,text="Add",command=add)
add.pack()

deletebutton = Button(window,text="Delete",command=deletebutton)
deletebutton.pack()

window.mainloop()
